from htmldom import htmldom
dom = htmldom.HtmlDom("http://kubernetes.io/")  
dom = dom.createDom()
p_links = dom.find("a")  
for link in p_links:
  print ("URL: " +link.attr("href"))
