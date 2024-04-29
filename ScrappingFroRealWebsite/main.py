from bs4 import BeautifulSoup
import requests
import time
print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')
def find_jobs():


    html = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').text.replace(' ', '')
        if 'Posted1dayago' in published_date or 'Posted2daysago' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/job{index}.txt', 'w') as f:
                    f.write(f'Company name: {company_name.strip()} \n')
                    f.write(f'Skills: {skills.strip()} \n')
                    f.write(f'More info: {more_info} \n')
                print(f'File saved job{index}.txt')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_waiting = 10
        print(f'Finding job every {time_waiting} minutes..')
        time.sleep(time_waiting*60)