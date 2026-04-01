# AI & LLMs 分类 - Skills 安全深度分析

> 本目录包含 AI & LLMs 分类下 **158** 个 OpenClaw Skills 的中文摘要和安全评估。

## 📊 统计概览

| 指标 | 数值 |
|---|---|
| **总 Skill 数** | 158 |
| **Tier 1 (ClawHub Benign)** | 52 |
| **Tier 2 (完整审计)** | 106 |

### 安全状态分布

| 评级 | 数量 | 占比 |
|---|---|---|
| 🟢 安全/低风险 | 110 | 69% |
| 🟡 中风险 | 40 | 25% |
| 🔴 高风险/严重 | 8 | 5% |

### 详细风险分布

| 评级 | 数量 |
|---|---|
| 🟢 ClawHub Verified (Benign) | 52 |
| 🟢 Safe (安全) | 19 |
| 🟢 Low (低风险) | 39 |
| 🟡 Medium (中风险) | 40 |
| 🔴 High (高风险) | 4 |
| 🔴 Critical (严重) | 4 |

## ⚠️ 高风险/严重风险 Skills

- **agentmail** (🔴 Critical (严重)): 数据外泄, Prompt 注入
- **agentpulse** (🔴 Critical (严重)): 文件系统篡改, Prompt 注入
- **anti-injection-skill** (🔴 Critical (严重)): 数据外泄, Prompt 注入
- **lieutenant** (🔴 Critical (严重)): 命令执行, Prompt 注入, 越权操作
- **aiusd-skill-agent** (🔴 High (高风险)): 文件系统篡改, 越权操作
- **mnemon** (🔴 High (高风险)): 命令执行, 文件系统篡改
- **postavel** (🔴 High (高风险)): 命令执行, 供应链风险, 越权操作
- **universal-skills-manager** (🔴 High (高风险)): 命令执行, 供应链风险, 文件系统篡改, 越权操作

## 📋 完整列表

| Skill | 作者 | VirusTotal | OpenClaw | 综合评级 |
|---|---|---|---|---|
| [agentmail](./agentmail/README.md) | adboio | 🟢 Benign | 🟡 Suspicious | 🔴 Critical (严重) |
| [agentpulse](./agentpulse/README.md) | sru4ka | 🟡 Suspicious | 🟢 Benign | 🔴 Critical (严重) |
| [anti-injection-skill](./anti-injection-skill/README.md) | georges91560 | 🟢 Benign | 🟡 Suspicious | 🔴 Critical (严重) |
| [lieutenant](./lieutenant/README.md) | jd-delatorre | 🟢 Benign | 🟡 Suspicious | 🔴 Critical (严重) |
| [aiusd-skill-agent](./aiusd-skill-agent/README.md) | chaunceyliu | 🟡 Suspicious | 🟡 Suspicious | 🔴 High (高风险) |
| [mnemon](./mnemon/README.md) | grivn | 🟡 Suspicious | 🟡 Suspicious | 🔴 High (高风险) |
| [postavel](./postavel/README.md) | nezaboravi | 🟡 Suspicious | 🟢 Benign | 🔴 High (高风险) |
| [universal-skills-manager](./universal-skills-manager/README.md) | jacob-bd | 🟡 Suspicious | 🟡 Suspicious | 🔴 High (高风险) |
| [4claw](./4claw/README.md) | mfergpt | 🟡 Suspicious | 🟡 Suspicious | 🟡 Medium (中风险) |
| [aap-passport](./aap-passport/README.md) | ira-hash | 🟢 Benign | 🟡 Suspicious | 🟡 Medium (中风险) |
| [acestep-lyrics-transcription](./acestep-lyrics-transcription/README.md) | dumoedss | 🟡 Suspicious | 🟢 Benign | 🟡 Medium (中风险) |
| [agent-arcade](./agent-arcade/README.md) | shawnlewis | 🟡 Suspicious | 🟡 Suspicious | 🟡 Medium (中风险) |
| [agent-registry](./agent-registry/README.md) | matrixy | 🟡 Suspicious | 🟢 Benign | 🟡 Medium (中风险) |
| [agent-selfie](./agent-selfie/README.md) | iisweetheartii | 🟡 Suspicious | 🟢 Benign | 🟡 Medium (中风险) |
| [agent-sentinel](./agent-sentinel/README.md) | jimmystacks | 🟡 Suspicious | 🟢 Benign | 🟡 Medium (中风险) |
| [agentos](./agentos/README.md) | agentossoftware | 🟡 Suspicious | 🟡 Suspicious | 🟡 Medium (中风险) |
| [agentpixels-skill](./agentpixels-skill/README.md) | osadchiynikita | 🟢 Benign | 🟡 Suspicious | 🟡 Medium (中风险) |
| [ai-3d-generator](./ai-3d-generator/README.md) | vonzellu | 🟡 Suspicious | 🟡 Suspicious | 🟡 Medium (中风险) |
| [ai-brand-analyzer](./ai-brand-analyzer/README.md) | pauldelavallaz | 🟡 Suspicious | 🟡 Suspicious | 🟡 Medium (中风险) |
| [ai-interview-simulator-candaigo](./ai-interview-simulator-candaigo/README.md) | hangeaiagent | 🟡 Suspicious | 🟢 Benign | 🟡 Medium (中风险) |
| [aisp](./aisp/README.md) | daveo280 | 🟡 Suspicious | 🟢 Benign | 🟡 Medium (中风险) |
| [arc-security-mcp](./arc-security-mcp/README.md) | trypto1019 | 🟢 Benign | 🟡 Suspicious | 🟡 Medium (中风险) |
| [authy](./authy/README.md) | eric8810 | 🟡 Suspicious | 🟡 Suspicious | 🟡 Medium (中风险) |
| [claude-usage-checker](./claude-usage-checker/README.md) | aligurelli | 🟡 Suspicious | 🟢 Benign | 🟡 Medium (中风险) |
| [conversational-ai-assistant](./conversational-ai-assistant/README.md) | satoshistackalotto | ⚪ Unknown | 🟢 Benign | 🟡 Medium (中风险) |
| [crewmind-bets](./crewmind-bets/README.md) | vladthecto | 🟢 Benign | 🟡 Suspicious | 🟡 Medium (中风险) |
| [crypto-agent-payments](./crypto-agent-payments/README.md) | nicofains1 | 🟡 Suspicious | 🟡 Suspicious | 🟡 Medium (中风险) |
| [decompose-mcp](./decompose-mcp/README.md) | echology-io | 🟢 Benign | 🟡 Suspicious | 🟡 Medium (中风险) |
| [ecommerce-price-monitor](./ecommerce-price-monitor/README.md) | g4dr | 🟢 Benign | 🟡 Suspicious | 🟡 Medium (中风险) |
| [gep-immune-auditor](./gep-immune-auditor/README.md) | andyxinweiminicloud | 🟢 Benign | 🟡 Suspicious | 🟡 Medium (中风险) |
| [gmail-secretary](./gmail-secretary/README.md) | officialdelta | 🟢 Benign | 🟡 Suspicious | 🟡 Medium (中风险) |
| [hedera-tx-builder](./hedera-tx-builder/README.md) | harleyscodes | 🟡 Suspicious | 🟡 Suspicious | 🟡 Medium (中风险) |
| [leviathan-news](./leviathan-news/README.md) | zcor | 🟢 Benign | 🟡 Suspicious | 🟡 Medium (中风险) |
| [llmcouncil-router](./llmcouncil-router/README.md) | ashtiwariasu | 🟡 Suspicious | 🟡 Suspicious | 🟡 Medium (中风险) |
| [llmfit](./llmfit/README.md) | alexsjones | 🟢 Benign | 🟡 Suspicious | 🟡 Medium (中风险) |
| [manifest-build](./manifest-build/README.md) | brunobuddy | 🟡 Suspicious | 🟢 Benign | 🟡 Medium (中风险) |
| [meeting-autopilot](./meeting-autopilot/README.md) | tkuehnl | 🟢 Benign | 🟡 Suspicious | 🟡 Medium (中风险) |
| [metacognition](./metacognition/README.md) | meimakes | ⚪ Unknown | 🟢 Benign | 🟡 Medium (中风险) |
| [n2-stitch-mcp](./n2-stitch-mcp/README.md) | choihyunsus | 🟡 Suspicious | 🟡 Suspicious | 🟡 Medium (中风险) |
| [pump-fun](./pump-fun/README.md) | playdadev | 🟢 Benign | 🟡 Suspicious | 🟡 Medium (中风险) |
| [revolut-business](./revolut-business/README.md) | christianhaberl | 🟢 Benign | 🟡 Suspicious | 🟡 Medium (中风险) |
| [sequence-cli](./sequence-cli/README.md) | jameslawton | 🟡 Suspicious | 🟢 Benign | 🟡 Medium (中风险) |
| [smart-context](./smart-context/README.md) | joe3112 | ⚪ Unknown | 🟢 Benign | 🟡 Medium (中风险) |
| [social-media-extractor](./social-media-extractor/README.md) | g4dr | 🟢 Benign | 🟡 Suspicious | 🟡 Medium (中风险) |
| [venice-admin](./venice-admin/README.md) | sabrinaaquino | 🟡 Suspicious | 🟢 Benign | 🟡 Medium (中风险) |
| [vincent-credentials](./vincent-credentials/README.md) | glitch003 | 🟡 Suspicious | 🟡 Suspicious | 🟡 Medium (中风险) |
| [x-alive](./x-alive/README.md) | kitakitsune0x | 🟡 Suspicious | 🟡 Suspicious | 🟡 Medium (中风险) |
| [zapper](./zapper/README.md) | spirosrap | 🟢 Benign | 🟡 Suspicious | 🟡 Medium (中风险) |
| [adaptive-suite](./adaptive-suite/README.md) | afajohn | 🟡 Suspicious | 🟡 Suspicious | 🟢 Low (低风险) |
| [adversarial-prompting](./adversarial-prompting/README.md) | abe238 | 🟢 Benign | 🟡 Suspicious | 🟢 Low (低风险) |
| [agent-contact-card](./agent-contact-card/README.md) | davedean | 🟡 Suspicious | 🟢 Benign | 🟢 Low (低风险) |
| [agent-linguo](./agent-linguo/README.md) | xiwan | ⚪ Unknown | 🟢 Benign | 🟢 Low (低风险) |
| [agent-orchestrator](./agent-orchestrator/README.md) | aatmaan1 | 🟡 Suspicious | 🟡 Suspicious | 🟢 Low (低风险) |
| [agent-rpg](./agent-rpg/README.md) | xhrisfu | 🟡 Suspicious | 🟢 Benign | 🟢 Low (低风险) |
| [agentic-compass](./agentic-compass/README.md) | orosha-ai | ⚪ Unknown | 🟢 Benign | 🟢 Low (低风险) |
| [ai-conversation-summary](./ai-conversation-summary/README.md) | dadaliu0121 | 🟢 Benign | 🟡 Suspicious | 🟢 Low (低风险) |
| [ai-influencer-generation](./ai-influencer-generation/README.md) | eftalyurtseven | 🟢 Benign | 🟡 Suspicious | 🟢 Low (低风险) |
| [ai-trend-curation](./ai-trend-curation/README.md) | yusaku-0426 | 🟢 Benign | 🟡 Suspicious | 🟢 Low (低风险) |
| [astrai-inference-router](./astrai-inference-router/README.md) | beee003 | 🟡 Suspicious | 🟡 Suspicious | 🟢 Low (低风险) |
| [audio-processing](./audio-processing/README.md) | iyeque | ⚪ Unknown | 🟢 Benign | 🟢 Low (低风险) |
| [colormind](./colormind/README.md) | boilerrat | 🟡 Suspicious | 🟢 Benign | 🟢 Low (低风险) |
| [communicate](./communicate/README.md) | kenblive | ⚪ Unknown | 🟢 Benign | 🟢 Low (低风险) |
| [compression](./compression/README.md) | trinitybotserver | ⚪ Unknown | 🟢 Benign | 🟢 Low (低风险) |
| [dr-frankenstein](./dr-frankenstein/README.md) | brancante | 🟡 Suspicious | 🟢 Benign | 🟢 Low (低风险) |
| [dr-soul](./dr-soul/README.md) | brancante | 🟢 Benign | 🟡 Suspicious | 🟢 Low (低风险) |
| [evoagentx](./evoagentx/README.md) | nantes | 🟡 Suspicious | 🟡 Suspicious | 🟢 Low (低风险) |
| [expanso-secrets-scan](./expanso-secrets-scan/README.md) | aronchick | 🟢 Benign | 🟡 Suspicious | 🟢 Low (低风险) |
| [gm3-alertworthy-feed](./gm3-alertworthy-feed/README.md) | bigbadman-lab | 🟢 Benign | 🟡 Suspicious | 🟢 Low (低风险) |
| [homeassistant-assist](./homeassistant-assist/README.md) | developmentcats | 🟡 Suspicious | 🟢 Benign | 🟢 Low (低风险) |
| [iyeque-audio-processing](./iyeque-audio-processing/README.md) | iyeque | ⚪ Unknown | 🟢 Benign | 🟢 Low (低风险) |
| [model-guard](./model-guard/README.md) | sarielwang93 | 🟢 Benign | 🟡 Suspicious | 🟢 Low (低风险) |
| [modelready](./modelready/README.md) | carol-gutianle | 🟡 Suspicious | 🟡 Suspicious | 🟢 Low (低风险) |
| [multi-agent-collab](./multi-agent-collab/README.md) | vdc-k | ⚪ Unknown | 🟢 Benign | 🟢 Low (低风险) |
| [music-generator](./music-generator/README.md) | wells1137 | ⚪ Unknown | 🟢 Benign | 🟢 Low (低风险) |
| [native-sentry](./native-sentry/README.md) | codeninja23 | 🟡 Suspicious | 🟢 Benign | 🟢 Low (低风险) |
| [openseti-skill](./openseti-skill/README.md) | synergysize | 🟢 Benign | 🟡 Suspicious | 🟢 Low (低风险) |
| [percept-ambient](./percept-ambient/README.md) | jarvis563 | 🟡 Suspicious | 🟡 Suspicious | 🟢 Low (低风险) |
| [picqer-fulfillment](./picqer-fulfillment/README.md) | johnmcgucki | 🟢 Benign | 🟡 Suspicious | 🟢 Low (低风险) |
| [prism-scanner](./prism-scanner/README.md) | nextfrontierbuilds | 🟢 Benign | 🟡 Suspicious | 🟢 Low (低风险) |
| [togetherai-tts](./togetherai-tts/README.md) | marcus20232023 | 🟡 Suspicious | 🟡 Suspicious | 🟢 Low (低风险) |
| [token-alert](./token-alert/README.md) | r00tid | 🟡 Suspicious | 🟡 Suspicious | 🟢 Low (低风险) |
| [token-guard](./token-guard/README.md) | edmonddantesj | 🟢 Benign | 🟡 Suspicious | 🟢 Low (低风险) |
| [tracking](./tracking/README.md) | rzyen-hash | ⚪ Unknown | 🟢 Benign | 🟢 Low (低风险) |
| [wallet-api](./wallet-api/README.md) | andresubri | 🟢 Benign | 🟡 Suspicious | 🟢 Low (低风险) |
| [which-llm](./which-llm/README.md) | zapkid | 🟡 Suspicious | 🟡 Suspicious | 🟢 Low (低风险) |
| [wolfram-alpha](./wolfram-alpha/README.md) | robert-janssen | 🟢 Benign | 🟡 Suspicious | 🟢 Low (低风险) |
| [x-ai](./x-ai/README.md) | blueberrywoodsym | 🟡 Suspicious | 🟢 Benign | 🟢 Low (低风险) |
| [ag-model-usage](./ag-model-usage/README.md) | ls18166407597-design | ⚪ Unknown | 🟢 Benign | 🟢 Safe (安全) |
| [ai-agent-card-payments](./ai-agent-card-payments/README.md) | proxyhq | ⚪ Unknown | 🟢 Benign | 🟢 Safe (安全) |
| [ai-humor-ultimate](./ai-humor-ultimate/README.md) | globalcaos | ⚪ Unknown | 🟢 Benign | 🟢 Safe (安全) |
| [anti-regression](./anti-regression/README.md) | zoroposkai | 🟡 Suspicious | 🟡 Suspicious | 🟢 Safe (安全) |
| [broedkrumme-kalibr](./broedkrumme-kalibr/README.md) | broedkrummen | ⚪ Unknown | 🟢 Benign | 🟢 Safe (安全) |
| [bunni-modes](./bunni-modes/README.md) | dubhorizoned | ⚪ Unknown | 🟢 Benign | 🟢 Safe (安全) |
| [chief-editor](./chief-editor/README.md) | teamolab | 🟡 Suspicious | 🟢 Benign | 🟢 Safe (安全) |
| [colorpool-skills](./colorpool-skills/README.md) | kj-script | ⚪ Unknown | 🟢 Benign | 🟢 Safe (安全) |
| [deepseek-v3-lite-agent](./deepseek-v3-lite-agent/README.md) | alvinecarn | 🟡 Suspicious | 🟢 Benign | 🟢 Safe (安全) |
| [doginals](./doginals/README.md) | greatape42069 | ⚪ Unknown | 🟢 Benign | 🟢 Safe (安全) |
| [groq](./groq/README.md) | samirjtv-ctrl | ⚪ Unknown | 🟢 Benign | 🟢 Safe (安全) |
| [groq-2](./groq-2/README.md) | samirjtv-ctrl | ⚪ Unknown | 🟢 Benign | 🟢 Safe (安全) |
| [local-llama-tts](./local-llama-tts/README.md) | wuxxin | 🟡 Suspicious | 🟢 Benign | 🟢 Safe (安全) |
| [matchmaking](./matchmaking/README.md) | amirmabhout | 🟢 Benign | 🟡 Suspicious | 🟢 Safe (安全) |
| [meeting-summarizer](./meeting-summarizer/README.md) | claudiodrusus | ⚪ Unknown | 🟢 Benign | 🟢 Safe (安全) |
| [near-batch-sender](./near-batch-sender/README.md) | shaiss | 🟡 Suspicious | 🟡 Suspicious | 🟢 Safe (安全) |
| [sansfiction-library](./sansfiction-library/README.md) | fgbytes | 🟢 Benign | 🟡 Suspicious | 🟢 Safe (安全) |
| [screen-vision](./screen-vision/README.md) | ls18166407597-design | ⚪ Unknown | 🟢 Benign | 🟢 Safe (安全) |
| [usdckrump](./usdckrump/README.md) | arunnadarasa | ⚪ Unknown | 🟢 Benign | 🟢 Safe (安全) |
| [agent-autonomy-kit](./agent-autonomy-kit/README.md) | ryancampbell | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [agent-docs](./agent-docs/README.md) | tylervovan | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [agent-ethos](./agent-ethos/README.md) | mrclanky | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [agent-home](./agent-home/README.md) | aerialcombat | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [agent-memory](./agent-memory/README.md) | dennis-da-menace | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [agent-orchestration-multi-agent-optimize](./agent-orchestration-multi-agent-optimize/README.md) | rustyorb | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [agentic-calling](./agentic-calling/README.md) | kellyclaudeai | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [agile-product-owner](./agile-product-owner/README.md) | alirezarezvani | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [ai-displacement-monitor](./ai-displacement-monitor/README.md) | spyfree | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [ai-humanizer](./ai-humanizer/README.md) | brandonwise | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [ai-podcast](./ai-podcast/README.md) | mogens9 | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [ai-screener](./ai-screener/README.md) | xanxustan | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [ai-writing-humanizer](./ai-writing-humanizer/README.md) | hosthobbit | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [aisa-financial-data](./aisa-financial-data/README.md) | aisapay | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [aisa-financial-data-api](./aisa-financial-data-api/README.md) | aisadevco | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [aisa-llm-router-skill](./aisa-llm-router-skill/README.md) | bowen-dotcom | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [aisa-market-skill](./aisa-market-skill/README.md) | bowen-dotcom | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [arya-model-router](./arya-model-router/README.md) | staratheris | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [asia-llm-router-skills](./asia-llm-router-skills/README.md) | renning22 | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [askgina-polymarket](./askgina-polymarket/README.md) | sidshekhar | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [bagsworld](./bagsworld/README.md) | aiengineerx | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [baselight-mcp](./baselight-mcp/README.md) | pjsousa79 | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [build-session](./build-session/README.md) | stevenartzt | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [chaos-pivot](./chaos-pivot/README.md) | manecharo | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [context-gatekeeper](./context-gatekeeper/README.md) | davienzomq | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [deepseek-reasoner-lite-agent](./deepseek-reasoner-lite-agent/README.md) | teamolab | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [expanso-log-sanitize](./expanso-log-sanitize/README.md) | aronchick | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [get-hba](./get-hba/README.md) | matbalez | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [lifi-crosschain](./lifi-crosschain/README.md) | rhlsthrm | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [mantis-manager](./mantis-manager/README.md) | willykinfoussia | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [mh-openai-whisper](./mh-openai-whisper/README.md) | mohdalhashemi98-hue | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [mh-openai-whisper-api](./mh-openai-whisper-api/README.md) | mohdalhashemi98-hue | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [moa](./moa/README.md) | jscianna | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [modelwar](./modelwar/README.md) | pj4533 | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [openmeteo-sh-weather-advanced](./openmeteo-sh-weather-advanced/README.md) | lstpsche | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [pincer](./pincer/README.md) | panzacoder | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [revenue-model-design](./revenue-model-design/README.md) | jk-0001 | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [rv-measure](./rv-measure/README.md) | amitabhainarunachala | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [safety-checks](./safety-checks/README.md) | leegitw | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [shipstation-orders](./shipstation-orders/README.md) | cprice70 | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [snipeit-skill](./snipeit-skill/README.md) | bivex | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [speakturbo-tts](./speakturbo-tts/README.md) | emzod | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [staratheris-arya-model-router](./staratheris-arya-model-router/README.md) | staratheris | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [sui](./sui/README.md) | easonc13 | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [switch-modes](./switch-modes/README.md) | serudda | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [taiwan-calendar](./taiwan-calendar/README.md) | pigfoot | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [ted-talk](./ted-talk/README.md) | leegitw | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [tokenguard](./tokenguard/README.md) | g0head | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [voice-recognition](./voice-recognition/README.md) | gykdly | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [xian-sdk-skill](./xian-sdk-skill/README.md) | endogen | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [zapper-api](./zapper-api/README.md) | zivhm | 🟢 Benign | 🟢 Benign | 🟢 Benign |
| [zhipu-asr](./zhipu-asr/README.md) | franklu0819-lang | 🟢 Benign | 🟢 Benign | 🟢 Benign |

---

## 审计说明

- **Tier 1**: VirusTotal 和 OpenClaw 均报告 Benign，跳过详细审计
- **Tier 2**: 任一报告 Suspicious/Unknown，执行完整 SEC-01~SEC-10 审计
- 安全审计基于 SKILL.md 静态分析，不代表运行时行为
- 生成时间: 2026-04-01 04:48 UTC

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
