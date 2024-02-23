def call_rest_api(verb, url, body, page):
  #
  headers = {
      'Content-Type': "application/json",
      #'User-Agent': "apache spark 3.x"
  }
  res = None
  # Make API request, get response object back, create dataframe from above schema.
  try:
    if verb == "get":
      res = requests.get("{url}/{page}".format(url=url,page=page), data=body, headers=headers)
    else:
      res = requests.post("{url}/{page}".format(url=url,page=page), data=body, headers=headers)
  except Exception as e:
    return e
  if res != None and res.status_code == 200:
    return json.loads(res.text)
  return None