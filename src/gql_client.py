from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport


# GraphQL client class입니다. 단순 Requests 모듈을 사용해서도 구현할 수 있지만, GraphQL 쿼리를 작성하는 데에는 해당 클라이언트를 사용하는 것이 더 편리합니다.
# 기본적으로 GraphQL API에 요청을 보낼 URL과 헤더를 초기화합니다.
class GraphQLClient:
    def __init__(self, url, token):
        if url is None:
            raise Exception("QUERY를 요청할 URL이 없습니다.")
        if token is None:
            raise Exception("Authorization token이 없습니다.")

        # 타임아웃 15초

        self.url = url
        self.token = "Bearer " + token
        self.transport = AIOHTTPTransport(
            url=self.url,
            headers={"content-type": "application/json", "Authorization": self.token},
            timeout=1500,
        )
        self.client = Client(
            transport=self.transport, fetch_schema_from_transport=False
        )

    def execute_query(self, query_str):
        query = gql(query_str)
        try:
            result = self.client.execute(query)
        except Exception as e:
            print(e)
            raise Exception("GraphQL API 요청에 실패했습니다.")
        return result
