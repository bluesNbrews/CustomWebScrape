function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  treat= require('treat')
  result={}
  for i=1,9,1
  do
  	assert(splash:runjs('document.querySelector("#proxylisttable_next a").click()'))
  	result[i]=splash:html()
  end
  return