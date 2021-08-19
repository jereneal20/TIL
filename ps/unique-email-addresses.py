class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        distinctEmails = set()
        for email in emails:
            # atIdx = email.find('@')
            local, domain = email.split('@')

            local = local.split('+')[0].replace('.', '')
            # if local.find('+') != -1:
            #     local = local[:local.find('+')]
            # local = local.replace(".", "")
            distinctEmails.add(local + '@' + domain)

        return len(distinctEmails)
