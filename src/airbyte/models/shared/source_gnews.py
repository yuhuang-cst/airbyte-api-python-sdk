"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, List, Optional

class Country(str, Enum):
    r"""This parameter allows you to specify the country where the news articles returned by the API were published, the contents of the articles are not necessarily related to the specified country. You have to set as value the 2 letters code of the country you want to filter."""
    AU = 'au'
    BR = 'br'
    CA = 'ca'
    CN = 'cn'
    EG = 'eg'
    FR = 'fr'
    DE = 'de'
    GR = 'gr'
    HK = 'hk'
    IN = 'in'
    IE = 'ie'
    IL = 'il'
    IT = 'it'
    JP = 'jp'
    NL = 'nl'
    NO = 'no'
    PK = 'pk'
    PE = 'pe'
    PH = 'ph'
    PT = 'pt'
    RO = 'ro'
    RU = 'ru'
    SG = 'sg'
    ES = 'es'
    SE = 'se'
    CH = 'ch'
    TW = 'tw'
    UA = 'ua'
    GB = 'gb'
    US = 'us'

class In(str, Enum):
    TITLE = 'title'
    DESCRIPTION = 'description'
    CONTENT = 'content'

class Language(str, Enum):
    AR = 'ar'
    ZH = 'zh'
    NL = 'nl'
    EN = 'en'
    FR = 'fr'
    DE = 'de'
    EL = 'el'
    HE = 'he'
    HI = 'hi'
    IT = 'it'
    JA = 'ja'
    ML = 'ml'
    MR = 'mr'
    NO = 'no'
    PT = 'pt'
    RO = 'ro'
    RU = 'ru'
    ES = 'es'
    SV = 'sv'
    TA = 'ta'
    TE = 'te'
    UK = 'uk'

class Nullable(str, Enum):
    TITLE = 'title'
    DESCRIPTION = 'description'
    CONTENT = 'content'

class SortBy(str, Enum):
    r"""This parameter allows you to choose with which type of sorting the articles should be returned. Two values  are possible:
      - publishedAt = sort by publication date, the articles with the most recent publication date are returned first
      - relevance = sort by best match to keywords, the articles with the best match are returned first
    """
    PUBLISHED_AT = 'publishedAt'
    RELEVANCE = 'relevance'

class Gnews(str, Enum):
    GNEWS = 'gnews'

class TopHeadlinesTopic(str, Enum):
    r"""This parameter allows you to change the category for the request."""
    BREAKING_NEWS = 'breaking-news'
    WORLD = 'world'
    NATION = 'nation'
    BUSINESS = 'business'
    TECHNOLOGY = 'technology'
    ENTERTAINMENT = 'entertainment'
    SPORTS = 'sports'
    SCIENCE = 'science'
    HEALTH = 'health'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGnews:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API Key"""
    query: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query') }})
    r"""This parameter allows you to specify your search keywords to find the news articles you are looking for. The keywords will be used to return the most relevant articles. It is possible to use logical operators  with keywords. - Phrase Search Operator: This operator allows you to make an exact search. Keywords surrounded by
      quotation marks are used to search for articles with the exact same keyword sequence. 
      For example the query: \"Apple iPhone\" will return articles matching at least once this sequence of keywords.
    - Logical AND Operator: This operator allows you to make sure that several keywords are all used in the article
      search. By default the space character acts as an AND operator, it is possible to replace the space character 
      by AND to obtain the same result. For example the query: Apple Microsoft is equivalent to Apple AND Microsoft
    - Logical OR Operator: This operator allows you to retrieve articles matching the keyword a or the keyword b.
      It is important to note that this operator has a higher precedence than the AND operator. For example the 
      query: Apple OR Microsoft will return all articles matching the keyword Apple as well as all articles matching 
      the keyword Microsoft
    - Logical NOT Operator: This operator allows you to remove from the results the articles corresponding to the
      specified keywords. To use it, you need to add NOT in front of each word or phrase surrounded by quotes.
      For example the query: Apple NOT iPhone will return all articles matching the keyword Apple but not the keyword
      iPhone
    """
    country: Optional[Country] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    r"""This parameter allows you to specify the country where the news articles returned by the API were published, the contents of the articles are not necessarily related to the specified country. You have to set as value the 2 letters code of the country you want to filter."""
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'exclude': lambda f: f is None }})
    r"""This parameter allows you to filter the articles that have a publication date smaller than or equal to the  specified value. The date must respect the following format: YYYY-MM-DD hh:mm:ss (in UTC)"""
    in_: Optional[List[In]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('in'), 'exclude': lambda f: f is None }})
    r"""This parameter allows you to choose in which attributes the keywords are searched. The attributes that can be set are title, description and content. It is possible to combine several attributes."""
    language: Optional[Language] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('language'), 'exclude': lambda f: f is None }})
    nullable: Optional[List[Nullable]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nullable'), 'exclude': lambda f: f is None }})
    r"""This parameter allows you to specify the attributes that you allow to return null values. The attributes that  can be set are title, description and content. It is possible to combine several attributes"""
    sortby: Optional[SortBy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sortby'), 'exclude': lambda f: f is None }})
    r"""This parameter allows you to choose with which type of sorting the articles should be returned. Two values  are possible:
      - publishedAt = sort by publication date, the articles with the most recent publication date are returned first
      - relevance = sort by best match to keywords, the articles with the best match are returned first
    """
    SOURCE_TYPE: Final[Gnews] = dataclasses.field(default=Gnews.GNEWS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'exclude': lambda f: f is None }})
    r"""This parameter allows you to filter the articles that have a publication date greater than or equal to the  specified value. The date must respect the following format: YYYY-MM-DD hh:mm:ss (in UTC)"""
    top_headlines_query: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('top_headlines_query'), 'exclude': lambda f: f is None }})
    r"""This parameter allows you to specify your search keywords to find the news articles you are looking for. The keywords will be used to return the most relevant articles. It is possible to use logical operators  with keywords. - Phrase Search Operator: This operator allows you to make an exact search. Keywords surrounded by
      quotation marks are used to search for articles with the exact same keyword sequence. 
      For example the query: \"Apple iPhone\" will return articles matching at least once this sequence of keywords.
    - Logical AND Operator: This operator allows you to make sure that several keywords are all used in the article
      search. By default the space character acts as an AND operator, it is possible to replace the space character 
      by AND to obtain the same result. For example the query: Apple Microsoft is equivalent to Apple AND Microsoft
    - Logical OR Operator: This operator allows you to retrieve articles matching the keyword a or the keyword b.
      It is important to note that this operator has a higher precedence than the AND operator. For example the 
      query: Apple OR Microsoft will return all articles matching the keyword Apple as well as all articles matching 
      the keyword Microsoft
    - Logical NOT Operator: This operator allows you to remove from the results the articles corresponding to the
      specified keywords. To use it, you need to add NOT in front of each word or phrase surrounded by quotes.
      For example the query: Apple NOT iPhone will return all articles matching the keyword Apple but not the keyword
      iPhone
    """
    top_headlines_topic: Optional[TopHeadlinesTopic] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('top_headlines_topic'), 'exclude': lambda f: f is None }})
    r"""This parameter allows you to change the category for the request."""
    

