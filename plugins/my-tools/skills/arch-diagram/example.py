"""예시 시스템(문서 자동 갱신 파이프라인)의 아키텍처 구조도 생성 스크립트.
사용: python3 example.py "2026-01-01 09:00 KST" out.html
새 그림은 이 파일을 복사해 build()의 좌표와 SHARE 내용만 바꾼다."""
import sys, html
from pathlib import Path
STAMP=sys.argv[1]
OUT=sys.argv[2] if len(sys.argv)>2 else 'out.html'
HEAD=(Path(__file__).parent/'head.html').read_text()

def T(x,y,s,c=''):
    cls=f' class="{c}"' if c else ''
    return f'      <text{cls} x="{x}" y="{y}">{html.escape(s)}</text>\n'
def TM(x,y,s,c=''):
    cls=f' class="{c}"' if c else ''
    return f'      <text{cls} x="{x}" y="{y}" text-anchor="middle">{html.escape(s)}</text>\n'
def box(x,y,w,h,lines,c='box'):
    o=f'      <rect class="{c}" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>\n'
    yy=y+24
    for i,(s,k) in enumerate(lines):
        o+=T(x+16,yy,s,k); yy+=(18 if h<=56 else 22) if i==0 else 20
    return o
def chip(x,y,w,s):
    return f'      <rect class="chip" x="{x}" y="{y}" width="{w}" height="20" rx="10"/>\n'+TM(x+w/2,y+14,s,'s')
def L(pts,c='ln',m='ah'):
    return f'      <polyline class="{c}" points="{pts}" marker-end="url(#{m})"/>\n'

def build(D, test):
    o='    <svg viewBox="0 0 1290 745" role="img" aria-label="'+html.escape(D['aria'])+'">\n'
    o+='''      <defs>
        <marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head" d="M0 0 L10 5 L0 10 z"/></marker>
        <marker id="aa" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head a" d="M0 0 L10 5 L0 10 z"/></marker>
        <marker id="aw" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head w" d="M0 0 L10 5 L0 10 z"/></marker>
      </defs>
'''
    # left column
    o+=box(40,40,240,110,D['gitlab'])
    jx=110 if test else 40; jw=280-jx
    o+=box(jx,240,jw,100,D['jenkins'])
    o+=L(f'{jx+jw//2},150 {jx+jw//2},238')+T(jx+jw//2+8,198,D['jtrig'],'s')
    o+=L('280,290 330,290 330,140 398,140')+T(336,132,'받아감','s')
    if test:
        o+=box(40,430,240,122,D['b93'])+chip(222,438,50,'임시')
        o+=L('70,150 70,428')+T(78,402,'fetch','s')
        o+=L('280,490 350,490 350,170 398,170')+T(356,163,'scp','s')
    # 가운데 서버 구역
    o+='      <rect class="vm" x="380" y="30" width="520" height="600" rx="10"/>\n'+T(396,56,D['vm42'],'h')
    o+=f'      <text class="m" x="884" y="56" text-anchor="end">{html.escape(D["vm42sub"])}</text>\n'
    o+=box(400,80,240,120,D['deploy'])
    o+=L('520,200 520,220')+T(528,214,'성공','s')
    o+='      <rect class="pill" x="400" y="222" width="240" height="30" rx="15"/>\n'+TM(520,242,D['record'],'mono' if test else '')
    o+=L('640,190 660,190 660,237 678,237','ln w','aw')+T(665,214,'실패','sw')
    o+='      <rect class="pill w" x="680" y="222" width="200" height="30" rx="15"/>\n'+TM(780,242,D['fail'],'sw')
    o+='      <rect class="group" x="395" y="275" width="490" height="340" rx="8"/>\n'+T(411,298,D['agent'],'t')
    if test: o+=chip(813,284,56,'설치 전')
    o+=L('600,252 600,318','ln a','aa')+T(608,270,'이어서 실행','sa')
    o+=box(410,320,230,90,D['watch'])
    o+=box(410,430,190,50,D['repo'])+L('500,410 500,428')+T(508,424,'비교','s')
    o+=L('630,410 630,498','ln a','aa')+T(636,458,'등록','sa')
    o+=box(410,500,230,90,D['db'])
    o+=L('640,520 670,520 670,400 698,400','ln a','aa')+T(674,470,'꺼냄','sa')
    o+=box(700,320,180,150,D['worker'])
    o+=box(700,540,180,52,D['api'])+L('698,566 642,566')
    # cluster
    o+='      <rect class="cl" x="940" y="30" width="330" height="310" rx="10"/>\n'+T(956,56,D['cl'],'h')
    o+=f'      <text class="m" x="1254" y="56" text-anchor="end">{html.escape(D["clsub"])}</text>\n'
    for i,n in enumerate(D['nodes']):
        y=76+i*76
        o+=box(960,y,290,56,n)
        if i<2: o+=L(f'1105,{y+56} 1105,{y+74}')
    o+=T(956,320,D['clfoot'],'m')
    o+=L('640,100 958,100')+TM(800,92,'한 대씩 교체','s')
    o+=L('880,380 1000,380 1000,342','ln a','aa')+T(1018,366,D['capture'],'sa')
    # openai
    o+=box(980,420,290,90,D['openai'])
    o+=L('880,445 978,445','ln a','aa')+TM(930,437,'텍스트만','sa')
    # review
    o+=L('880,462 930,462 930,688 902,688')+T(936,600,'검토 대기','s')
    o+=box(400,660,500,56,D['review'],'box plan')
    o+=L('400,688 18,688 18,105 38,105','ln d')+T(30,680,'반영 (수동)','s')
    tags=[(1,40,40),(2,jx,240),(3,400,80),(4,940,30),(5,400,237),(6,410,320),(7,410,500),(8,700,320),(9,1000,361),(10,980,420),(11,400,660),(12,18,400)]
    if test: tags.append((2,40,430))
    o+='      <g class="tags">\n'+''.join(f'        <circle cx="{x}" cy="{y}" r="10"/><text x="{x}" y="{y+4}">{n}</text>\n' for n,x,y in tags)+'      </g>\n    </svg>\n'
    return o

m='m'; t='t'; n=''
SHARE=dict(
 aria='앱 코드가 바뀌면 CI가 빌드하고, 에이전트 서버의 배포 스크립트가 앱 클러스터 3노드를 차례로 교체한다. 하나라도 실패하면 전부 되돌리고 실패를 기록한다. 성공하면 배포 기록을 남기고 이어서 변경 감지가 돌아, 클러스터 화면을 캡처하고 AI로 문서 수정안을 만든다. 사람이 검수해 문서 레포에 반영하면, 문서만 따로 빌드해 앱 재시작 없이 클러스터의 문서 파일만 바로 교체한다.',
 gitlab=[('Git 서버',t),('앱 레포 · main',n),('문서 레포 · main',n),('git.example.com',m)],
 jtrig='코드·문서 변경',
 jenkins=[('CI 서버 · 10.0.0.10:8080',t),('앱: 매일 22시 확인 → 바이너리 빌드',n),('문서: 10분마다 확인 → 문서만 빌드',n),('바뀐 경우에만 빌드 · 커밋 SHA 보관',m)],
 vm42='에이전트 서버 · 10.0.0.20', vm42sub='',
 deploy=[('배포 스크립트',t),('앱 변경: 매일 00:00',n),('문서 변경: 바로 반영 · 재시작 없음',n),('새 빌드가 없으면 스크립트 종료',n),('한 대씩 교체 · 실패 시 전부 롤백',m)],
 record='배포 기록 (커밋 SHA)', fail='실패 기록 · 사람 확인',
 agent='문서 에이전트',
 watch=[('변경 감지',t),('지난 배포 → 이번 배포 사이',n),('바뀐 파일·커밋 메시지',m)],
 repo=[('앱 코드 기록',t),('비교만 함',m)],
 db=[('작업 DB',t),('작업 큐',n),('변경 기록',n)],
 worker=[('Worker',t),('고칠 문서 찾기',n),('바뀐 화면 캡처',n),('AI로 수정안 작성',n),('웹·PDF 빌드',n),('검토 대기로 넘김',m)],
 api=[('API',t),('수동 요청',m)],
 cl='앱 클러스터', clsub='데모',
 nodes=[[('node-01 · 10.0.1.11',t),('캡처 대상',m)],[('node-02 · 10.0.1.12',t),('앱 서버',m)],[('node-03 · 10.0.1.13',t),('앱 서버',m)]],
 clfoot='demo.example.com · 공유 스토리지',
 capture='화면 캡처 · node-01',
 openai=[('외부 AI API',t),('문장 수정·검수',n),('텍스트만, 저장 안 함',m)],
 review=[('사람 검수 → 문서 레포 반영',t),('반영되면 문서만 빌드해 바로 배포 · 검수 없는 자동 게시 없음',m)],
)
def page(title,sub,svg,test):
    legend='      <span><i></i>자동으로 동작</span>\n      <span><i class="d"></i>'+('예정 또는 사람이 함' if test else '사람이 함')+'</span>\n      <span><i class="a"></i>배포 → 문서 수정안 흐름</span>\n      <span><i class="w"></i>실패 시</span>\n'
    h=HEAD.replace('{{TITLE}}',title)
    return h+f'''<main>
  <h1>{title}</h1>
  <p class="sub">{STAMP} 기준{" · "+sub if sub else ""}</p>
  <figure>
    <div class="scroll">
{svg}    </div>
    <div class="legend">
{legend}    </div>
  </figure>
</main>
</body>
</html>
'''

Path(OUT).write_text(page('[예시] 문서 자동 갱신 아키텍처','',build(SHARE,False),False))
print(OUT)
