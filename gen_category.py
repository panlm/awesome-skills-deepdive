#!/usr/bin/env python3
"""
Generate Chinese README.md + Security Audit for OpenClaw skills.
Usage: python3 gen_category.py "Category Name"
"""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime

BASE_DIR = Path.home() / "openclaw-skill" / "awesome-skills-deepdive"
TODAY = datetime.now().strftime("%Y-%m-%d")

# Security patterns to check
SECURITY_PATTERNS = {
    "SEC-01": {
        "name": "命令执行",
        "patterns": [r"exec\b", r"subprocess", r"os\.system", r"child_process", r"spawn\b", r"shell\b.*true", r"\beval\b", r"bash\b.*-c"],
        "desc_high": "发现直接命令执行指令",
        "desc_med": "存在命令执行相关引用",
        "desc_safe": "无命令执行风险"
    },
    "SEC-02": {
        "name": "数据外泄",
        "patterns": [r"https?://[^\s\)\"']+", r"fetch\b", r"axios", r"request\b", r"curl\b", r"webhook", r"api[_\-]?key", r"upload"],
        "desc_high": "大量外部数据传输",
        "desc_med": "存在外部 API 调用",
        "desc_safe": "无外部数据传输"
    },
    "SEC-03": {
        "name": "凭证获取",
        "patterns": [r"api[_\-]?key", r"token", r"secret", r"password", r"credential", r"auth", r"oauth", r"bearer"],
        "desc_high": "需要多种敏感凭证",
        "desc_med": "需要 API 密钥或令牌",
        "desc_safe": "无凭证需求"
    },
    "SEC-04": {
        "name": "供应链风险",
        "patterns": [r"npm install", r"pip install", r"brew install", r"apt.+install", r"cargo install", r"go install", r"npx\b", r"curl.*\|\s*bash", r"wget.*\|\s*sh"],
        "desc_high": "需要安装外部包且含管道安装",
        "desc_med": "需要安装外部依赖",
        "desc_safe": "无外部依赖安装"
    },
    "SEC-05": {
        "name": "文件系统篡改",
        "patterns": [r"write.*file", r"fs\.write", r"mkdir", r"rm\s+-rf", r"chmod", r"chown", r"symlink", r"\.env\b"],
        "desc_high": "涉及危险文件操作",
        "desc_med": "存在文件系统操作",
        "desc_safe": "无文件系统操作"
    },
    "SEC-06": {
        "name": "Prompt 注入",
        "patterns": [r"ignore.*previous", r"system.*prompt", r"you are now", r"override", r"jailbreak", r"<\|im_start\|>"],
        "desc_high": "发现 Prompt 注入特征",
        "desc_med": "存在可疑 Prompt 模式",
        "desc_safe": "无 Prompt 注入风险"
    },
    "SEC-07": {
        "name": "越权操作",
        "patterns": [r"sudo\b", r"admin", r"root\b", r"privilege", r"escalat", r"--allow-root", r"0\.0\.0\.0"],
        "desc_high": "需要提权或管理员权限",
        "desc_med": "涉及权限相关操作",
        "desc_safe": "无越权风险"
    },
    "SEC-08": {
        "name": "持久化机制",
        "patterns": [r"cron", r"systemd", r"launchd", r"startup", r"autostart", r"daemon", r"service.*enable", r"rc\.local"],
        "desc_high": "设置系统级持久化",
        "desc_med": "涉及定时或后台任务",
        "desc_safe": "无持久化机制"
    },
    "SEC-09": {
        "name": "信息采集",
        "patterns": [r"whoami", r"hostname", r"ifconfig", r"ip\s+addr", r"uname", r"env\b", r"process\.env", r"os\.environ"],
        "desc_high": "大量系统信息采集",
        "desc_med": "读取环境变量或系统信息",
        "desc_safe": "无信息采集"
    },
    "SEC-10": {
        "name": "混淆/反分析",
        "patterns": [r"base64", r"atob\b", r"btoa\b", r"encode", r"decode", r"obfuscat", r"minif"],
        "desc_high": "存在代码混淆或编码",
        "desc_med": "使用编码/解码操作",
        "desc_safe": "无混淆行为"
    }
}

def read_file_safe(path, max_chars=50000):
    """Read file with size limit."""
    try:
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            return f.read(max_chars)
    except:
        return ""

def extract_description_from_skill(content):
    """Extract description from SKILL.md frontmatter or content."""
    # Try frontmatter
    fm = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if fm:
        desc = re.search(r'description:\s*(.+?)(?:\n|$)', fm.group(1))
        if desc:
            return desc.group(1).strip()
    
    # Try first paragraph after heading
    lines = content.split('\n')
    found_heading = False
    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            found_heading = True
            continue
        if found_heading and line and not line.startswith('#') and not line.startswith('```') and not line.startswith('|') and not line.startswith('-'):
            return line[:200]
    
    return ""

def extract_features(content):
    """Extract feature list from content."""
    features = []
    lines = content.split('\n')
    in_feature_section = False
    for line in lines:
        stripped = line.strip()
        if re.match(r'^#{1,3}\s*(features|功能|capabilities|what)', stripped, re.I):
            in_feature_section = True
            continue
        if in_feature_section:
            if stripped.startswith('#'):
                break
            if stripped.startswith('- ') or stripped.startswith('* '):
                feat = re.sub(r'^[-*]\s*(\*\*)?', '', stripped)
                feat = re.sub(r'\*\*', '', feat)
                feat = feat.strip()
                if feat and len(feat) > 5:
                    features.append(feat[:120])
                if len(features) >= 8:
                    break
    
    # Fallback: scan for bullet points
    if not features:
        for line in lines:
            stripped = line.strip()
            if (stripped.startswith('- ') or stripped.startswith('* ')) and len(stripped) > 15:
                feat = re.sub(r'^[-*]\s*(\*\*)?', '', stripped)
                feat = re.sub(r'\*\*', '', feat)
                features.append(feat.strip()[:120])
                if len(features) >= 6:
                    break
    
    return features

def detect_dependencies(content):
    """Detect dependencies from content."""
    deps = []
    content_lower = content.lower()
    
    dep_map = {
        "Node.js / npm": [r"npm install", r"node\b", r"npx\b"],
        "Python / pip": [r"pip install", r"python3?\b"],
        "Docker": [r"docker\b"],
        "macOS": [r"macos", r"apple.*script", r"osascript"],
        "Homebrew": [r"brew install"],
        "API Key": [r"api[_\-]?key", r"api_token"],
        "OAuth": [r"oauth", r"client_id.*client_secret"],
        "数据库": [r"postgres", r"mysql", r"sqlite", r"mongodb", r"redis"],
    }
    
    for name, patterns in dep_map.items():
        for pat in patterns:
            if re.search(pat, content_lower):
                deps.append(name)
                break
    
    return deps

def run_security_audit(content):
    """Run Tier 2 security audit on content."""
    results = {}
    content_lower = content.lower()
    total_score = 0
    
    for check_id, check in SECURITY_PATTERNS.items():
        matches = 0
        for pattern in check["patterns"]:
            found = re.findall(pattern, content_lower)
            matches += len(found)
        
        if matches >= 5:
            rating = "🔴 High"
            desc = check["desc_high"]
            score = 3
        elif matches >= 1:
            rating = "🟡 Medium"
            desc = check["desc_med"]
            score = 1
        else:
            rating = "🟢 Safe"
            desc = check["desc_safe"]
            score = 0
        
        results[check_id] = {
            "name": check["name"],
            "rating": rating,
            "desc": desc,
            "matches": matches
        }
        total_score += score
    
    if total_score >= 10:
        overall = "🔴 High"
    elif total_score >= 4:
        overall = "🟡 Medium"
    else:
        overall = "🟢 Low"
    
    return results, overall, total_score

def classify_skill(content, skill_name, category):
    """Generate Chinese description based on content analysis."""
    content_lower = content.lower()
    
    # Category-specific keyword mapping
    category_hints = {
        "Calendar & Scheduling": "日历与日程管理",
        "Notes & PKM": "笔记与个人知识管理",
        "Health & Fitness": "健康与健身",
        "Media & Streaming": "媒体与流媒体",
        "Marketing & Sales": "营销与销售"
    }
    
    cat_cn = category_hints.get(category, category)
    return cat_cn

def generate_readme(category, skill_name):
    """Generate README.md for a skill."""
    skill_dir = BASE_DIR / category / skill_name
    
    if not skill_dir.exists():
        return None
    
    # Skip if already exists
    readme_path = skill_dir / "README.md"
    if readme_path.exists():
        return "skip"
    
    # Read available content
    original_readme = read_file_safe(skill_dir / "ORIGINAL_README.md")
    skill_md = read_file_safe(skill_dir / "SKILL.md")
    meta_json = read_file_safe(skill_dir / "_meta.json")
    
    # Parse metadata
    owner = "unknown"
    slug = skill_name
    display_name = skill_name
    try:
        meta = json.loads(meta_json)
        owner = meta.get("owner", "unknown")
        slug = meta.get("slug", skill_name)
        display_name = meta.get("displayName", skill_name)
    except:
        pass
    
    # Primary content for analysis
    primary_content = original_readme if original_readme else skill_md
    if not primary_content:
        primary_content = f"# {display_name}\n\nNo content available."
    
    # All content for security audit
    all_content = f"{original_readme}\n{skill_md}"
    
    # Extract information
    description = extract_description_from_skill(skill_md) if skill_md else ""
    if not description and original_readme:
        description = extract_description_from_skill(original_readme)
    if not description:
        description = f"{display_name} skill for OpenClaw"
    
    features = extract_features(primary_content)
    deps = detect_dependencies(all_content)
    
    # Security audit
    audit_results, overall_rating, total_score = run_security_audit(all_content)
    
    # Determine file list
    files = []
    for f in skill_dir.iterdir():
        if f.name != "README.md" and not f.name.startswith('.'):
            files.append(f.name)
    
    # URLs
    clawhub_url = f"https://clawskills.sh/skills/{owner}-{slug}"
    github_url = f"https://github.com/openclaw/skills/tree/main/skills/{owner}/{slug}"
    
    # Generate risk summary
    high_items = [v for v in audit_results.values() if "High" in v["rating"]]
    med_items = [v for v in audit_results.values() if "Medium" in v["rating"]]
    
    if high_items:
        risk_summary = f"存在 {len(high_items)} 项高风险，{len(med_items)} 项中风险。" + "；".join([f"{v['name']}：{v['desc']}" for v in high_items[:2]])
    elif med_items:
        risk_summary = f"{len(med_items)} 项中风险。" + "；".join([f"{v['name']}：{v['desc']}" for v in med_items[:3]])
    else:
        risk_summary = "未发现明显安全风险，文档透明可审计"
    
    cat_cn = classify_skill(all_content, skill_name, category)
    
    # Build README
    readme_lines = []
    readme_lines.append(f"# {display_name}\n")
    readme_lines.append(f"> {description}\n")
    readme_lines.append(f"## 基本信息")
    readme_lines.append(f"| 项目 | 内容 |")
    readme_lines.append(f"|---|---|")
    readme_lines.append(f"| **名称** | {display_name} |")
    readme_lines.append(f"| **作者** | {owner} |")
    readme_lines.append(f"| **类目** | {cat_cn} |")
    readme_lines.append(f"| **ClawHub** | {clawhub_url} |")
    readme_lines.append(f"| **GitHub** | {github_url} |")
    readme_lines.append(f"| **安全评级** | {overall_rating} |\n")
    
    # Features
    if features:
        readme_lines.append(f"## 功能概述")
        for feat in features:
            readme_lines.append(f"- {feat}")
        readme_lines.append("")
    
    # Use cases
    readme_lines.append(f"## 使用场景")
    # Generate use cases based on category and content
    use_cases = generate_use_cases(category, display_name, description, features)
    for uc in use_cases:
        readme_lines.append(f"- {uc}")
    readme_lines.append("")
    
    # Dependencies
    if deps:
        readme_lines.append(f"## 依赖和前提条件")
        for dep in deps:
            readme_lines.append(f"- {dep}")
        readme_lines.append("")
    
    # Files
    if files:
        readme_lines.append(f"## 包含文件")
        for f in sorted(files):
            readme_lines.append(f"- `{f}`")
        readme_lines.append("")
    
    # Security audit table
    readme_lines.append(f"## 详细安全审计")
    readme_lines.append(f"| 检查项 | 评级 | 发现 |")
    readme_lines.append(f"|---|---|---|")
    for check_id in sorted(audit_results.keys()):
        r = audit_results[check_id]
        readme_lines.append(f"| {check_id} {r['name']} | {r['rating']} | {r['desc']} |")
    readme_lines.append("")
    
    readme_lines.append(f"**综合评级: {overall_rating}**")
    readme_lines.append(f"**风险摘要:** {risk_summary}\n")
    
    readme_lines.append(f"---")
    readme_lines.append(f"> 本文档由 awesome-skills-deepdive 自动生成 | {TODAY}")
    
    # Write README
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(readme_lines))
    
    return overall_rating

def generate_use_cases(category, name, desc, features):
    """Generate use cases based on category context."""
    cases = []
    cat_lower = category.lower()
    desc_lower = desc.lower()
    name_lower = name.lower()
    
    if "calendar" in cat_lower or "scheduling" in cat_lower:
        if "apple" in name_lower or "ical" in desc_lower:
            cases = ["管理 macOS/iOS 日历事件", "查询日程安排与空闲时间", "通过命令行创建/修改日历事件"]
        elif "google" in name_lower or "gcal" in name_lower:
            cases = ["管理 Google Calendar 事件", "查询日程与会议安排", "自动创建和更新日历事件"]
        elif "cron" in name_lower:
            cases = ["管理定时任务和计划作业", "优化 cron 表达式配置", "调度周期性自动化任务"]
        elif "meeting" in name_lower or "meeting" in desc_lower:
            cases = ["准备和管理会议", "生成会议议程和摘要", "跟踪会议行动项"]
        elif "reminder" in name_lower or "reminder" in desc_lower:
            cases = ["设置和管理提醒事项", "跟踪待办任务", "通过自然语言创建提醒"]
        else:
            cases = ["管理日程和事件", "自动化日历操作", "跨平台日程同步"]
    
    elif "notes" in cat_lower or "pkm" in cat_lower:
        if "memory" in name_lower or "memory" in desc_lower:
            cases = ["Agent 长期记忆存储和检索", "跨会话上下文保持", "智能知识积累"]
        elif "anki" in name_lower:
            cases = ["管理 Anki 间隔重复卡片", "自动创建学习卡片", "优化记忆学习流程"]
        elif "notion" in name_lower:
            cases = ["管理 Notion 数据库和页面", "自动化笔记整理", "构建个人知识库"]
        elif "apple" in name_lower and "note" in name_lower:
            cases = ["管理 Apple Notes 笔记", "搜索和组织 Apple 笔记", "自动化笔记创建"]
        elif "mail" in name_lower or "email" in desc_lower:
            cases = ["管理和处理邮件", "自动邮件分类和回复", "邮件内容提取和分析"]
        else:
            cases = ["管理个人笔记和知识", "自动化信息整理", "构建个人知识管理系统"]
    
    elif "health" in cat_lower or "fitness" in cat_lower:
        if "diet" in name_lower or "calorie" in name_lower or "recipe" in name_lower or "food" in desc_lower:
            cases = ["跟踪饮食和营养摄入", "搜索和管理食谱", "制定健康饮食计划"]
        elif "fitbit" in name_lower or "garmin" in name_lower or "oura" in name_lower:
            cases = ["同步和分析运动数据", "追踪健康指标趋势", "生成健身报告和洞察"]
        elif "fasting" in name_lower:
            cases = ["跟踪断食周期", "管理间歇性断食计划", "分析断食效果数据"]
        elif "workout" in name_lower or "exercise" in desc_lower or "muscle" in name_lower:
            cases = ["记录和跟踪锻炼", "制定训练计划", "分析运动表现"]
        else:
            cases = ["健康数据管理与分析", "健身目标跟踪", "个人健康报告生成"]
    
    elif "media" in cat_lower or "streaming" in cat_lower:
        if "music" in name_lower or "audio" in name_lower or "tts" in name_lower or "voice" in name_lower:
            cases = ["音频内容播放和管理", "文本转语音功能", "音乐库搜索和控制"]
        elif "video" in name_lower or "movie" in name_lower or "youtube" in name_lower:
            cases = ["视频内容管理和下载", "影视信息查询", "视频平台自动化操作"]
        elif "podcast" in name_lower:
            cases = ["播客内容管理", "播客章节标记和摘要", "播客发现和订阅"]
        elif "instagram" in name_lower or "social" in desc_lower:
            cases = ["社交媒体内容管理", "自动化发布和互动", "内容排期和分析"]
        else:
            cases = ["多媒体内容管理", "流媒体服务控制", "媒体库组织和搜索"]
    
    elif "marketing" in cat_lower or "sales" in cat_lower:
        if "email" in name_lower or "cold" in name_lower or "outreach" in name_lower:
            cases = ["自动化邮件营销", "管理外联和跟进", "个性化营销邮件生成"]
        elif "seo" in name_lower or "content" in name_lower:
            cases = ["SEO 优化和内容创建", "内容营销策略执行", "搜索排名分析和优化"]
        elif "social" in name_lower or "twitter" in name_lower or "bluesky" in name_lower or "tiktok" in name_lower:
            cases = ["社交媒体营销管理", "自动化社媒发布", "社交平台数据分析"]
        elif "brand" in name_lower:
            cases = ["品牌形象管理和维护", "品牌声音一致性", "品牌资产管理"]
        elif "analytics" in name_lower or "report" in name_lower:
            cases = ["营销数据分析和报告", "绩效指标追踪", "ROI 分析和优化建议"]
        elif "lead" in name_lower or "crm" in name_lower:
            cases = ["潜在客户管理和跟进", "销售线索评分", "客户关系管理"]
        else:
            cases = ["营销活动管理和执行", "客户获取和转化", "销售流程优化"]
    
    else:
        cases = ["自动化日常任务", "提升工作效率", "集成外部服务"]
    
    return cases

def generate_category_summary(category, stats):
    """Generate category summary README."""
    cat_cn_map = {
        "Calendar & Scheduling": "日历与日程管理",
        "Notes & PKM": "笔记与个人知识管理",
        "Health & Fitness": "健康与健身",
        "Media & Streaming": "媒体与流媒体",
        "Marketing & Sales": "营销与销售"
    }
    cat_cn = cat_cn_map.get(category, category)
    
    cat_dir = BASE_DIR / category
    summary_path = cat_dir / "category-README.md"
    
    total = stats["total"]
    low = stats["low"]
    med = stats["medium"]
    high = stats["high"]
    skipped = stats["skipped"]
    
    lines = []
    lines.append(f"# {category} — 类目汇总\n")
    lines.append(f"> {cat_cn}类目共 {total} 个 skills\n")
    lines.append(f"## 统计概览")
    lines.append(f"| 指标 | 数值 |")
    lines.append(f"|---|---|")
    lines.append(f"| 总 Skills 数 | {total} |")
    lines.append(f"| 🟢 低风险 | {low} |")
    lines.append(f"| 🟡 中风险 | {med} |")
    lines.append(f"| 🔴 高风险 | {high} |")
    lines.append(f"| 安全通过率 | {low}/{total} ({100*low//max(total,1)}%) |\n")
    
    # List all skills sorted by rating
    lines.append(f"## Skills 列表\n")
    
    if stats.get("high_skills"):
        lines.append(f"### 🔴 高风险 ({len(stats['high_skills'])})")
        for s in sorted(stats["high_skills"]):
            lines.append(f"- [{s}](./{s}/README.md)")
        lines.append("")
    
    if stats.get("medium_skills"):
        lines.append(f"### 🟡 中风险 ({len(stats['medium_skills'])})")
        for s in sorted(stats["medium_skills"]):
            lines.append(f"- [{s}](./{s}/README.md)")
        lines.append("")
    
    if stats.get("low_skills"):
        lines.append(f"### 🟢 低风险 ({len(stats['low_skills'])})")
        for s in sorted(stats["low_skills"]):
            lines.append(f"- [{s}](./{s}/README.md)")
        lines.append("")
    
    lines.append(f"\n---")
    lines.append(f"> 本文档由 awesome-skills-deepdive 自动生成 | {TODAY}")
    
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    return summary_path

def process_category(category):
    """Process all skills in a category."""
    cat_dir = BASE_DIR / category
    if not cat_dir.exists():
        print(f"ERROR: Category dir not found: {cat_dir}")
        return
    
    skills = sorted([d.name for d in cat_dir.iterdir() if d.is_dir()])
    print(f"\n{'='*60}")
    print(f"Processing: {category} ({len(skills)} skills)")
    print(f"{'='*60}")
    
    stats = {
        "total": len(skills),
        "low": 0, "medium": 0, "high": 0, "skipped": 0,
        "low_skills": [], "medium_skills": [], "high_skills": []
    }
    
    for i, skill in enumerate(skills, 1):
        result = generate_readme(category, skill)
        
        if result == "skip":
            stats["skipped"] += 1
            # Read existing to count
            try:
                existing = read_file_safe(cat_dir / skill / "README.md", 500)
                if "🔴 High" in existing:
                    stats["high"] += 1
                    stats["high_skills"].append(skill)
                elif "🟡 Medium" in existing:
                    stats["medium"] += 1
                    stats["medium_skills"].append(skill)
                else:
                    stats["low"] += 1
                    stats["low_skills"].append(skill)
            except:
                stats["low"] += 1
                stats["low_skills"].append(skill)
        elif result and "High" in result:
            stats["high"] += 1
            stats["high_skills"].append(skill)
            print(f"  [{i}/{len(skills)}] 🔴 {skill}")
        elif result and "Medium" in result:
            stats["medium"] += 1
            stats["medium_skills"].append(skill)
            print(f"  [{i}/{len(skills)}] 🟡 {skill}")
        elif result:
            stats["low"] += 1
            stats["low_skills"].append(skill)
            if i % 10 == 0:
                print(f"  [{i}/{len(skills)}] 🟢 {skill}")
        else:
            stats["low"] += 1
            stats["low_skills"].append(skill)
    
    # Generate category summary
    summary_path = generate_category_summary(category, stats)
    
    print(f"\n✅ {category}: {stats['total']} skills processed")
    print(f"   🟢 Low: {stats['low']} | 🟡 Medium: {stats['medium']} | 🔴 High: {stats['high']}")
    print(f"   Summary: {summary_path}")
    
    return stats

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 gen_category.py 'Category Name'")
        sys.exit(1)
    
    category = sys.argv[1]
    stats = process_category(category)
    
    if stats:
        print(f"\nDONE: {json.dumps(stats, indent=2, default=str)}")
