from django.shortcuts import render, resolve_url, redirect, render_to_response, reverse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from web.selectFromDb import *
from web.client import *

# Create your views here.

classify_list = []  # 用于存储分类
get_art = ''''''
article = '''
魔兽世界：争霸艾泽拉斯重回起点，大结局或提前出现？伏笔太多！

魔兽世界陪伴了勇士们已经10年了，在这10年里很多我们称之为“神”的BOSS，都已经被脚男们推到。而魔兽世界的主线历史背景似乎也穷途末路，随着游戏策划们创意的枯竭，暴雪迫切需要一个版本来填坑过度，所以8.0争霸艾泽拉斯应运而生。

魔兽世界：争霸艾泽拉斯重回起点，大结局或提前出现？伏笔太多！


争霸艾泽拉斯

在我们击败黑暗泰坦萨格拉斯的时候，勇士们发现有一个更大的阴谋笼罩着整个宇宙。似乎萨格拉斯的燃烧军团并不是只是为了单纯的杀戮，从这个大版本最后的结局中，我们发现隐藏再虚空背后有一个连泰坦众神都害怕的敌人——虚空！

看完魔兽这样的故事走向，我越来越觉得这个以魔幻为题材的游戏，却有点像星际争霸的剧情了。邪恶的虫群最后也被洗白，最后三族联盟共同面对宇宙中最强的BOSS“艾蒙”。

难道最后我们艾泽拉斯也会联手泰坦众神，还有燃烧军团一起抵抗最大的敌人虚空吗？

魔兽世界：争霸艾泽拉斯重回起点，大结局或提前出现？伏笔太多！

萨格拉斯

争霸艾泽拉斯这个版本，虽然表面上是联盟与部落阵营的一场大冲突，可是在这冲突之下也隐藏着巨大的伏笔！而萨格拉斯最后怒劈艾泽拉斯星球的那把神剑，最后也一定能成为一个重要的“引子”。

而两个阵营的冲突更是让我们有很多想不通的疑点，比如希尔瓦娜斯为何火烧泰达希尔？在共同抵御了燃烧军团以后，希女王肯定不会无缘无故的去做贸然撕毁盟约的事情。

而最有可能的情况就是，泰达希尔的根部已经被上古之神腐化了，而上古之神就是虚空的爪牙！

魔兽世界：争霸艾泽拉斯重回起点，大结局或提前出现？伏笔太多！

火烧泰达希尔

最后让我们想想魔兽争霸WAR3的开场动画，当联盟和部落在大战一触即发的时候，天空突然被邪能笼罩，漫天开始落下火雨和恶魔......而这样的场景，是否会在“争霸艾泽拉斯”版本的最后出现呢？

虚空突然被撕裂，上古之神拔地而起，众神齐聚艾泽拉斯，而艾泽拉斯的星魂成为了最强的泰坦参与战斗，这也许就是魔兽世界的大结局吧！                                                                                                                                                                  7月15日
'''

source = '''
魔兽世界：争霸艾泽拉斯重回起点，大结局或提前出现？伏笔太多！

魔兽世界陪伴了勇士们已经10年了，在这10年里很多我们称之为“神”的BOSS，都已经被脚男们推到。而魔兽世界的主线历史背景似乎也穷途末路，随着游戏策划们创意的枯竭，暴雪迫切需要一个版本来填坑过度，所以8.0争霸艾泽拉斯应运而生。

魔兽世界：争霸艾泽拉斯重回起点，大结局或提前出现？伏笔太多！


争霸艾泽拉斯

在我们击败黑暗泰坦萨格拉斯的时候，勇士们发现有一个更大的阴谋笼罩着整个宇宙。似乎萨格拉斯的燃烧军团并不是只是为了单纯的杀戮，从这个大版本最后的结局中，我们发现隐藏再虚空背后有一个连泰坦众神都害怕的敌人——虚空！

看完魔兽这样的故事走向，我越来越觉得这个以魔幻为题材的游戏，却有点像星际争霸的剧情了。邪恶的虫群最后也被洗白，最后三族联盟共同面对宇宙中最强的BOSS“艾蒙”。

难道最后我们艾泽拉斯也会联手泰坦众神，还有燃烧军团一起抵抗最大的敌人虚空吗？

魔兽世界：争霸艾泽拉斯重回起点，大结局或提前出现？伏笔太多！

萨格拉斯

争霸艾泽拉斯这个版本，虽然表面上是联盟与部落阵营的一场大冲突，可是在这冲突之下也隐藏着巨大的伏笔！而萨格拉斯最后怒劈艾泽拉斯星球的那把神剑，最后也一定能成为一个重要的“引子”。

而两个阵营的冲突更是让我们有很多想不通的疑点，比如希尔瓦娜斯为何火烧泰达希尔？在共同抵御了燃烧军团以后，希女王肯定不会无缘无故的去做贸然撕毁盟约的事情。

而最有可能的情况就是，泰达希尔的根部已经被上古之神腐化了，而上古之神就是虚空的爪牙！

魔兽世界：争霸艾泽拉斯重回起点，大结局或提前出现？伏笔太多！

火烧泰达希尔

最后让我们想想魔兽争霸WAR3的开场动画，当联盟和部落在大战一触即发的时候，天空突然被邪能笼罩，漫天开始落下火雨和恶魔......而这样的场景，是否会在“争霸艾泽拉斯”版本的最后出现呢？

虚空突然被撕裂，上古之神拔地而起，众神齐聚艾泽拉斯，而艾泽拉斯的星魂成为了最强的泰坦参与战斗，这也许就是魔兽世界的大结局吧！                                                                                                                                                                  7月15日
'''
def index(request):
    '''
    访问ip或域名跳转到aboutUs页面
    :param request:
    :return:
    '''
    return redirect(resolve_url(about_us))


def about_us(request):
    '''
    返回aboutUS页面
    :param request:
    :return:
    '''
    return render(request,'aboutUS.html')


def hot_news(request):
    '''
    查询热点新闻数据库，
    将返回结果进行分页操作。
    :param request:
    :return:
    '''
    info_dict = select()  # 查询数据库
    for item in info_dict:
        print ('12')
        print (item)
    pageinator = Paginator(info_dict, 6, 2)  # 将查询到的结果分页。
    page = request.GET.get('page')  # 从url里获取参数。

    try:
        customer = pageinator.page(page)  # 获取当前参数的页面数据。
    except PageNotAnInteger:
        customer = pageinator.page(1)
    except EmptyPage:
        customer = pageinator.page(pageinator.num_pages)
    return render(request, 'hotNews.html', {'cus_list':customer})  # 渲染模板并返回。


def article_analyze(request):
    global get_art, classify_list
    text = get_art
    list = classify_list
    if request.method == 'GET':
        get_art = ''''''
        classify_list = []
        return render(request, 'articleAnalyze.html',{'classify': list,'article': article,'get_art': text})

def get_article(request):
    if request.method == 'POST':
        global classify_list,get_art
        classify_list = []
        text = request.POST.get('text')  # 获取form里的text。
        if len(text.strip()) < 300:
            print(len(text.strip()))
            classify = '文字小于三百个字符，自动恢复为默认范文1。'  # 通过tcp传输文字 并获取返回的分类。
            get_art = source
        else:
            print(len(text.strip()))
            get_art = text
            classify = sen_info(text)  # 通过tcp传输文字 并获取返回的分类。
            # classify = '123'

        classify_list.append(classify)  # 添加分类。



        return redirect(resolve_url(article_analyze))  # 页面跳转。
    return redirect(resolve_url(about_us))


def page_not_found(request):
    return render_to_response('404.html')

