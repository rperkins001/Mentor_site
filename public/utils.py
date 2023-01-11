from django.db.models import Q
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def compute_score(result, query):
    # Calculate the score based on the query and the result
    score = 0
    if query in result.first_name:
        score += 1
    if query in result.last_name:
        score += 1
    if query in result.company:
        score += 1
    if query in result.industry:
        score += 1
    return score

def rank_results(results, query):
    ranked_results = []
    for result in results:
        # Compute a score for the result based on the query
        score = compute_score(result, query)
        ranked_results.append((result, score))
    # Sort the results by score
    ranked_results.sort(key=lambda x: x[1], reverse=True)
    return ranked_results





def paginateProfiles(request, profiles, results):
    page = request.GET.get('page')
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, profiles


def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    #skills = Skill.objects.filter(name__icontains=search_query)

    #profiles = Profile.objects.distinct().filter(
    #    Q(name__icontains=search_query) |
    #    Q(short_intro__icontains=search_query) |
    #    Q(skill__in=skills)
    #)

    #return profiles, search_query
