from app.libs.http import Http

class search_on_tfl:
    url='https://api.tfl.gov.uk/Search?query={}&app_id=daa74ccf&app_key=a090b25d115a59e79df24282fe30abeb'
    @classmethod
    def search_by_query(cls,query):
        url=cls.url.format(query)
        result=Http.get(url)

        return result
















