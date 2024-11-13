import sys
import json
from awsip import find_ip, download_aws_ip_set

sys.stdout.write(json.dumps(find_ip(download_aws_ip_set(), sys.argv[1]), indent=2))