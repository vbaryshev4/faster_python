class ActiveJobs:
    def __init__(self, log):
        self.log = log

    def is_active(self, job_id):
        for k in self.log.keys():
            if job_id < k:
                batch_log = self.log[k]
                if batch_log['info_by'] == 'open':
                    return job_id in batch_log['vals']
                else:
                    return job_id not in batch_log['vals']



if __name__ == '__main__':
    batches = {
        1000: {'info_by': 'open', 'last_val': 999, 'vals': [10, 555]},
        2000: {'info_by': 'open', 'last_val': 1999, 'vals': [1900, 1921]},
        3000: {'info_by': 'closed', 'last_val': 2701, 'vals': [2551, 2602, 2701]}
    }

    test_cases = [(999, False), (1900, True), (2700, True)]
    j = ActiveJobs(batches)
    for t in test_cases:
        job_id, expected = t
        print(j.is_active(job_id), expected)
