#! /usr/bin/env python
import requests
import json
"""This is a program the go to facebook to just display t0 10 posts of a public site, it requres a valid tooken because facebook has restrction around it's graph API
this script also requires to know the page_id/company_id """
class SocialData():
    def __init__(self, company_id, access_token):
        self.company_id = company_id
        self.access_token = access_token
        self.posts = {"posts":[]}
        self.data_holder = self.posts["posts"]

    def collect_posts(self):
     
        graph_url= "https://graph.facebook.com/v3.1/{}/feed?access_token={}".format(self.company_id ,self.access_token)
        # print(myUrl)
        head = {'Authorization': 'access_token {}'.format(self.access_token)}
        response = requests.get(graph_url)
        print("http response code:",response.status_code, response.reason)
        data = response.json()
        resp_data = json.loads(json.dumps(data, sort_keys=True, indent=4))
        
        
        posts_count = 0
        #loop through the response to get each item           
        for element in resp_data['data']:
            if ('message' in element) and ('id' in element) and ('created_time' in element) and  posts_count<11:
                self.data_holder.append({'created_time':element['created_time']})
                self.data_holder.append({'user':element['id']})
                self.data_holder.append({'post':element['message']})
                self.data_holder.append({'count':posts_count})
                posts_count  += 1    

    def write_posts(self):
        file_path='/tmp/data.json'
        with open(file_path, 'w') as outfile:
            print("writing file to: ",file_path)
            json.dump(self.posts, outfile) 

        print("done")


if __name__ == '__main__':

    valid_company_id = "64067037679" 
    valid_access_token ="EAAGvnR99JukBAG8csFrlo0MYvwSEJtnXM2JPZBCSgRb1BaAqn0SxCi4vZCD4eYg4F5qgcyXfbQ6Ig49a1A2mv5m9fcaeNcpRxVnKw38ybN0Yneb6a5DYVyDxxb7DpUu2IiZAmkeViwpY2spFXxmvgmmJ7uSRTWwZBpNdP09BYd80Bo1PytIHctvxgTWJgIGNpS1SH7FtAAZDZD"    

    socialData = SocialData(valid_company_id,valid_access_token) 
    socialData.collect_posts()
    socialData.write_posts()
