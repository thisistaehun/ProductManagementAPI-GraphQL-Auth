import os
import sys

from data_service import DataService
from gql_client import GraphQLClient
from gql_query_service import GraphQLQueryService
from http_service import HTTPService


class Main:
    # Main 클래스는 프로그램의 진입점입니다. 생성자에서 필요한 서비스 객체들을 초기화하고, 토큰을 받아와 GraphQL API에 요청을 보내는 클라이언트 객체를 생성합니다.
    def __init__(self):
        # HTTPService: 단순 HTTP 요청을 위한 서비스 객체입니다. 
        self.httpService = HTTPService()
        # DataService: 데이터를 여러 형태로 변환하고 저장하는 등의 활동을 위한 서비스 객체입니다.
        self.dataService = DataService()
        # GraphQLQueryService: GraphQL 쿼리를 생성하기 위한 서비스 객체입니다.
        self.gqlQueryService = GraphQLQueryService()
        # HTTPService를 통해 인증 토큰을 받아옵니다.
        self.token = self.httpService.getToken()
        # URL: GraphQL API의 엔드포인트입니다.
        self.url = os.getenv('QUERY_URL')
        # GraphQLClient: GraphQL API에 요청을 보내기 위한 클라이언트 객체입니다.
        self.client = GraphQLClient(self.url, self.token)

    # run 메서드에서 본격적으로 프로그램을 실행합니다. 
    # 1. 엑셀 파일을 읽어와서 데이터를 가져옵니다.
    # 2. 가져온 데이터를 GraphQL API에 요청할 수 있는 형태로 변환합니다.
    # 3. GraphQL API에 요청을 보내고, 응답을 받아옵니다.
    # 4. 응답을 JSON 파일로 저장합니다.
    def run(self):
        excelFileName = self.readLine()
        # 엑셀 파일을 읽어옵니다.
        excelFileData = self.dataService.getExcel(excelFileName)
        # 엑셀 파일의 데이터를 딕셔너리 형태로 변환합니다.
        dictionaryData = self.dataService.dfToDict(excelFileData)
        print(f'엑셀 파일 읽기 완료, 파일 이름: {excelFileName}.xlsx')
        responseData = []
        # 딕셔너리 형태로 변환된 데이터를 GraphQL API에 요청할 수 있는 형태로 변환합니다.
        # Loop를 돌면서 GraphQL API에 요청을 보내고, 응답을 받아와 JSON 형태로 저장합니다.
        for i, item in enumerate(dictionaryData):
            minPrice = item['Price_min']
            maxPrice = item['Price_max']
            category = item['CKey']
            first = item['first_num']
            # GraphQL API에 요청을 보내기 위한 쿼리를 생성합니다.
            input = f'''minPrice: {minPrice}, maxPrice: {maxPrice}, category: "{category}", first: {first}'''
            print(input)
            query = self.gqlQueryService.allItemsMini(input)
            # GraphQL API에 요청을 보내고, 응답을 받아옵니다.
            response = self.client.execute_query(query)
            print(response)
            # 응답을 responseData 변수에 추가합니다. 
            responseData.append({
                "seq": i + 1,
                "data": response
            })
            self.dataService.dictTOJsonFile(responseData, excelFileName + f'_temp_{i + 1}')
            print(f'{i + 1}번째 요청 완료')
        # 응답을 JSON 파일로 저장합니다.
        self.dataService.dictTOJsonFile(responseData, excelFileName)
        
            
    # 사용자로부터 엑셀 파일 이름을 입력받습니다.
    def readLine(self):
        print('엑셀 파일 이름을 입력하세요.(확장자 제외, 예시: test) : ')
        input = sys.stdin.readline().strip()
        return input


if __name__ == "__main__":
    main = Main()
    main.run()
    print('작업 완료!')
