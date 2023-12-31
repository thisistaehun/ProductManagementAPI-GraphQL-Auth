# v3 변경 사항

createEnv.bat 파일을 실행하면, 자동으로 가상환경을 생성하고, 의존성을 설치합니다.
이후 Run.bat 파일을 실행하면, 자동으로 프로그램이 구동됩니다.
구동 이후 진행은 기존과 동일하지만, 가상환경 진입 및 의존성 설치 과정을 생략할 수 있습니다.
추가로 데이터 저장 방식 및 쿼리 호출 변수 형태가 요청사항에 맞추어 변경되었습니다.

# 프로그램 사용 방법(mac OS 기준 터미널 환경)

본 프로그램은 엑셀 파일을 읽고, 오너플랜 API 서버에서 데이터를 받아와 JSON 파일로 저장하는 프로그램입니다.
해당 가이드를 천천히 읽어보시고, 프로그램을 실행해보세요. 실행중 문제가 발생하면 개발자에게 문의해주시기 바랍니다.

## 0. 가상환경 생성

예상치 못한 패키지 충돌을 방지하기 위해, pip에서 제공하는 가상환경을 사용합니다.
가상환경을 사용하기 위해서는, python 3.9 이상이 설치되어 있어야 합니다.
python 3.9 이상이 설치되어 있지 않다면, python 3.9 이상을 설치해주세요.

가상환경을 생성하려면, owner-clan-project 경로의 터미널에서 다음과 같은 명령어를 입력해주세요.

```bash
python3 -m venv owner_venv
```

## 1. 가상환경 진입

가상환경을 생성했다면, 가상환경에 진입해야 합니다.
가상환경에 진입하려면 owner-clan-project 경로의 터미널에서 다음과 같은 명령어를 입력해주세요.

```bash
source owner_venv/bin/activate
```

가상환경에 진입한 상태로, 프로그램을 구동시키면 됩니다.

가상환경에서 빠져나오려면 다음과 같은 명령어를 입력해주세요.

```bash
deactivate
```

## 2. 의존성 설치

프로그램 구동 전, 필요한 의존성들을 설치해야 합니다. 가상환경에 진입한 상태에서, 다음과 같은 명령어를 입력해주세요.

```bash
pip install -r requirements.txt
```

본 명령어는 owner-clan-project 경로에 있는 requirements.txt 파일을 참고하여, 필요한 의존성들을 설치합니다.

## 3. 프로그램 구동

프로그램을 구동하려면 다음과 같은 순서로 진행하시면 됩니다.

### 3.1. 엑셀 파일 추가

프로젝트 루트 경로(owner-clan-project)에 있는 input 폴더에 엑셀 파일을 넣어주세요.

### 3.2. 프로그램 구동

이제 프로그램을 구동할 차례입니다. 프로그램을 구동하기 위해서는, 다음과 같은 명령어를 입력해주세요.

```bash
python3 src/main.py
```

프로그램이 정상적으로 시작되면, 콘솔에 다음과 같은 문구가 출력됩니다.

```bash
토큰 발급 성공!
엑셀 파일 이름을 입력하세요.(확장자 제외, 예시: test) : 
```

엑셀 파일 이름을 입력하고 엔터를 누르면, 엑셀 파일을 읽기 시작합니다. 주의할 점은, 엑셀 파일 이름에 확장자를 제외한 이름만 입력해야 합니다. (예시: test.xlsx -> test)

정상적으로 엑셀 파일을 읽고, 작업이 수행된다면 다음과 같은 문구가 출력될 것입니다.

```bash
엑셀 파일 읽기 완료, 파일 이름: test.xlsx
1/3 저장 완료
2/3 저장 완료
3/3 저장 완료
작업 완료!
```

작업이 완료되면, output 폴더에 JSON 파일이 생성됩니다. 각 파일은 하나의 엑셀 파일에 대한 각 행의 데이터를 담고 있습니다.
# ProductManagementAPI-GraphQL-Auth
