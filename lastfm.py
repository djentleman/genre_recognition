# wrapper aorund api library to use last fm api
import api

def constructUrl(apiName, params):
    api_key = '8649be7c48a1034ae29f0e62b0bb3389'
    url = 'http://ws.audioscrobbler.com/2.0/' + '?method=' + apiName
    for key, value in params.iteritems():
        url += '&' + key + '=' + str(value)
    url += '&api_key=' + api_key
    return url

def getTrackTags(artistName, trackName, autocorrect=True, dump=False):
    params = {
                'artist': artistName,
                'track': trackName,
                'autocorrect': int(autocorrect),
                'format': 'json'
             }
    url = constructUrl('track.getTopTags', params)
    json = api.getJSON(url)
    # got the JSON, now parse out top tags
    numTopTags = 5
    tags = json['toptags']['tag']
    topTags = tags[0:min([numTopTags, len(tags)])]
    topTagNames = map(lambda x: x['name'], topTags)
    
    if dump:
        print "Artist: " + artistName
        print "Track: " + trackName
        for tag in topTagNames:
            print "     " + tag
        print "---------------------------"
        
    return topTagNames
    
    
if __name__ == '__main__':
    # test
    getTrackTags('Rise Against', 'Savior', dump=True)
    getTrackTags('The Wonder Years', 'Hoodie Weather', dump=True)
    getTrackTags('Andrew Jackson Jihad', 'Hate, Rain On Me', dump=True)
    getTrackTags('Netsky', 'Puppy', dump=True)
    
