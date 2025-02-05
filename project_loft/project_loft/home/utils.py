from django.db.models import Q
from django.contrib.postgres.search import (
    SearchQuery,
    SearchVector,
    SearchRank,
    SearchHeadline,
)
from goods.models import Product


def q_search(query):

    vector = SearchVector('title', 'category')
    query = SearchQuery(query)
    
    result = (
        Product.objects.annotate(rank=SearchRank(vector, query)).
        filter(rank__gt=0)
        .order_by('-rank')
    )

    result = result.annotate(
        headline=SearchHeadline(
            'title',
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel='</span>',
        )
    )
    
    
    result = result.annotate(
        bodyline=SearchHeadline(
            'category',
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel='</span>',
        )
    )
    
    return result

    
