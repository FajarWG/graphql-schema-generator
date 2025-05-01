import graphene

class LoginResponse_data(graphene.ObjectType):
    accessToken = graphene.String()

class LoginResponse(graphene.ObjectType):
    statusCode = graphene.Int()
    message = graphene.String()
    data = graphene.Field('LoginResponse_data')

class Projects_data_projects_project_status(graphene.ObjectType):
    topic_modelling = graphene.Boolean()
    sentiment = graphene.Boolean()
    emotion = graphene.Boolean()
    sna = graphene.Boolean()
    _id = graphene.String()

class Projects_data_projects(graphene.ObjectType):
    _id = graphene.String()
    title = graphene.String()
    description = graphene.String()
    keyword = graphene.String()
    userId = graphene.String()
    topic_category = graphene.String()
    language = graphene.String()
    start_date_crawl = graphene.String()
    end_date_crawl = graphene.String()
    createdAt = graphene.String()
    project_status = graphene.Field('Projects_data_projects_project_status')
    __v = graphene.Int()

class Projects_data(graphene.ObjectType):
    projects = graphene.List(graphene.Field('Projects_data_projects'))
    total = graphene.Int()
    page = graphene.Int()
    limit = graphene.Int()

class Projects(graphene.ObjectType):
    statusCode = graphene.Int()
    message = graphene.String()
    data = graphene.Field('Projects_data')

class Prompt_data_prompt_topik_1(graphene.ObjectType):
    optimal_prompt = graphene.String()
    pertanyaan = graphene.String()

class Prompt_data_prompt_topik_2(graphene.ObjectType):
    optimal_prompt = graphene.String()
    pertanyaan = graphene.String()

class Prompt_data_prompt_topik_3(graphene.ObjectType):
    optimal_prompt = graphene.String()
    pertanyaan = graphene.String()

class Prompt_data_prompt(graphene.ObjectType):
    topik_1 = graphene.List(graphene.Field('Prompt_data_prompt_topik_1'))
    topik_2 = graphene.List(graphene.Field('Prompt_data_prompt_topik_2'))
    topik_3 = graphene.List(graphene.Field('Prompt_data_prompt_topik_3'))

class Prompt_data(graphene.ObjectType):
    project_id = graphene.String()
    prompt = graphene.Field('Prompt_data_prompt')

class Prompt(graphene.ObjectType):
    data = graphene.Field('Prompt_data')

class Topic_data(graphene.ObjectType):
    context = graphene.String()
    keyword = graphene.String()
    projectId = graphene.String()
    topicId = graphene.Int()
    words = graphene.List(graphene.String())

class Topic(graphene.ObjectType):
    data = graphene.List(graphene.Field('Topic_data'))
    message = graphene.String()
    status = graphene.Int()

class SNA_data_links(graphene.ObjectType):
    full_text = graphene.String()
    source = graphene.String()
    source_community = graphene.Int()
    target = graphene.String()
    target_community = graphene.Int()
    topic = graphene.String()
    url_tweet = graphene.String()

class SNA_data_nodes(graphene.ObjectType):
    community = graphene.Int()
    id = graphene.String()
    name = graphene.String()
    profile_url = graphene.String()
    val = graphene.Int()

class SNA_data(graphene.ObjectType):
    links = graphene.List(graphene.Field('SNA_data_links'))
    nodes = graphene.List(graphene.Field('SNA_data_nodes'))
    projectId = graphene.String()

class SNA(graphene.ObjectType):
    data = graphene.List(graphene.Field('SNA_data'))
    total_data = graphene.Int()

