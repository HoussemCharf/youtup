import cgitb
from pytube import YouTube
from pydub import AudioSegment
def download (s,location):
  #defining quality

  format_type=['flv','mp4']
  quality=''
  fmt=''
  title=''
  #check if the url in youtube form
  if s.find("youtube.com/watch?v=") or s.find("youtu.be/watch?v="):
    yt = YouTube (s)
    Mult = yt.videos
    fmt = format_type[[i for i,x in enumerate(format_type) if x in str(Mult)][0]]
    title=yt.filename
    
    yt.filter(fmt)[0].resolution
    video= yt.get(fmt,yt.filter(fmt)[0].resolution)
    video.download(location)
    
    conmp3(yt.filename,fmt,title)
  else:
    print 'Error in URL Format please make sure'


def import_or_install():
  try:
    from pytube import YouTube
    from pydub import AudioSegment
  except ImportError:
    print 'make sure you have Pytube and pydub Libs in your machine \n else you can get them by pip install them'

def conmp3 (filename,fmt,title):
  file= open(title.join('.mp3'), 'wb')
  if fmt=='mp4':
    song = AudioSegment.from_file(filename,fmt)
    song.export(title.join('.mp3'),format='mp3')
    file.close()
  elif fmt=='flv':
    song = AudioSegment.from_file(filename,fmt)
    song.export(title.join('.mp3'),format='mp3')
    file.close()
  else:
    print 'Cant Converte format supported not found'


def  main():
  import_or_install()
  Url=raw_input("youtube Url:?")
  location=raw_input("Saving Location:?")
  if str(location)=='':
    download(str(Url),'\download')


if __name__ == "__main__":
    cgitb.enable()
    main()