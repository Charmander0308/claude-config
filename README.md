# claude-config

개인 Claude Code 플러그인 마켓플레이스.

공개 레포다. 예시·스킬에 실제 서버 주소, 사내 도메인, 제품명 등 내부 정보를 넣지 않고 가상의 값(예: `10.0.0.x`, `example.com`)을 쓴다.

## 설치 (PC마다 한 번)

```bash
claude plugin marketplace add Charmander0308/claude-config
claude plugin install my-tools@my-claude
```

## 업데이트

스킬을 고치면 `plugins/my-tools/.claude-plugin/plugin.json`의 `version`을 올려 푸시한다. 각 PC에서 아래 중 하나로 받는다.

터미널에서:

```bash
claude plugin marketplace update my-claude
claude plugin update my-tools@my-claude
```

Claude Code 채팅창에서:

- `/plugin` → **Marketplaces** 탭 → `my-claude` → **Update marketplace** (목록 갱신과 설치된 플러그인 업데이트를 한 번에 한다)
- 또는 `!`를 붙여 셸 명령으로: `! claude plugin marketplace update my-claude && claude plugin update my-tools@my-claude`

새 버전은 다음 세션부터 적용된다. 지금 세션에 바로 적용하려면 `/reload-plugins`를 실행한다.

## 들어 있는 스킬

- `arch-diagram`: 시스템·배포 아키텍처 구조도를 한 장짜리 HTML(SVG)로 그린다
- `notion-doc`: 도구·서비스·글을 조사해 노션 정리 문서를 정해진 양식으로 만든다

## 작업 규칙

`plugins/my-tools/rules.md`는 세션이 시작될 때 훅(`hooks/hooks.json`)으로 자동으로 들어간다.
