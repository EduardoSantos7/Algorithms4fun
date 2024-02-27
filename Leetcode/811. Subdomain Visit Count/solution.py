class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_subdomains = {}

        for cpdomain in cpdomains:
            count, subdomains = cpdomain.split(" ")
            subdomains = subdomains.split(".")
            for i, subdomain in enumerate(subdomains):
                domain = ".".join(subdomains[i:])
                curr_count = count_subdomains.get(domain)
                count_subdomains[domain] = int(count) if not curr_count else curr_count + int(count)
    
        return [" ".join([str(count), domain]) for domain, count in count_subdomains.items()]