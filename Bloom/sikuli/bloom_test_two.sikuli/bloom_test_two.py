click(Pattern("1437423112703.png").similar(0.80))
wait(1)
click("1437423171197.png")
wait(6)

if exists("1437423312752.png"):
    print "Success"
else:
    print "Fail!"
