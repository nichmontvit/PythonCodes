def email_list(domains):
    emails = []
    index = 0
    for domain in domains:
        for user in domains[domain]:
            emails.insert(index, user + "@" + domain)
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))