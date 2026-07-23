from collections import Counter
import re


class ClusteringService:

    @staticmethod
    def normalize(message:str):

        message=message.lower()

        message=re.sub(r'\d+','<num>',message)

        return message
    
    @staticmethod
    def cluster(logs):

        counter=Counter()

        for log in logs:

            normalized=ClusteringService.normalize(log["message"])
            counter[normalized]+=1
        
        clusters=[]

        for message,count in counter.items():

            clusters.append({
                "pattern":message,
                "count":count})
            
            clusters.sort(
                key=lambda x:x["count"],reverse=True
            )
            return clusters
        