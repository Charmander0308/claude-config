# claude-config

개인 Claude Code 플러그인 마켓플레이스.

공개 레포다. 예시·스킬에 실제 서버 주소, 사내 도메인, 제품명 등 내부 정보를 넣지 않고 가상의 값(예: `10.0.0.x`, `example.com`)을 쓴다.

## 설치 (PC마다 한 번)

```bash
claude plugin marketplace add Charmander0308/claude-config
claude plugin install my-tools@my-claude
```

## 업데이트

스킬을 고치면 `plugins/my-tools/.claude-plugin/plugin.json`의 `version`을 올려 푸시한다. 각 PC에서:

```bash
claude plugin marketplace update my-claude
claude plugin update my-tools@my-claude
```

## 들어 있는 스킬

- `arch-diagram`: 시스템·배포 아키텍처 구조도를 한 장짜리 HTML(SVG)로 그린다
