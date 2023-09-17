

# GraphQL 쿼리를 작성하는 서비스입니다. 해당 서비스에 다음과 같은 형태로 지속적으로 필요한 쿼리를 추가해서 사용할 수 있어요. 
class GraphQLQueryService:
    def allItemsMini(self, input):
        return f'''
        query {{
            allItems({input}) {{
                pageInfo {{
                    hasNextPage
                    hasPreviousPage
                    startCursor
                    endCursor
                }}
                edges {{
                    cursor
                    node {{
                        createdAt
                        updatedAt
                        key
                        name
                    }}
                }}
            }}
        }}
    '''

    
    def allItems(self, input):
        return f'''
            query {{
                allItems({input}) {{
                    pageInfo {{
                        hasNextPage
                        hasPreviousPage
                        startCursor
                        endCursor
                    }}
                    edges {{
                        cursor
                        node {{
                            createdAt
                            updatedAt
                            key
                            name
                            model
                            production
                            origin
                            id
                            price
                            pricePolicy
                            fixedPrice
                            searchKeywords
                            category {{
                                key
                                name
                                fullName
                            }}
                            content
                            shippingFee
                            shippingType
                            images(size: large)
                            status
                            options {{
                                optionAttributes {{
                                    name
                                    value
                                }}
                                price
                                quantity
                            }}
                            taxFree
                            adultOnly
                            returnable
                            noReturnReason
                            guaranteedShippingPeriod
                            openmarketSellable
                            boxQuantity
                            attributes
                            closingTime
                            returnCriteria
                            metadata
                        }}
                    }}
                }}
            }}
        '''