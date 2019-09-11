str = 'X-DSPAM-Confidence:0.8475'
locate = str.find(":")
end = str.find("5", locate)
final = float(str[locate+1 : end+1])
print (final)