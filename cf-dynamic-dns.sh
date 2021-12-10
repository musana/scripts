#!/bin/bash

# A bash script to update a Cloudflare DNS A record with the external IP of the source machine

# credit
# https://gist.githubusercontent.com/Ciantic/4e543f2d878a87a38c25032d5c727bf2/raw/63bed92f721c03bab23992406a162266825392ce/cloudflare-dyndns-a-aaaa-record-update.sh

# add as cronjob
# */5 * * * * /usr/local/bin/cf-ddns.sh > /dev/null 2>&1

# set your zone
zone=ZONE_WHICH_HOLDS_THE_RECORD # for ex: example.com

# set your domain
dnsrecord=A_RECORD_WHICH_WILL_BE_UPDATED # for ex: sub.example.com

## Cloudflare authentication details
cloudflare_auth_email=YOUR@MAIL.XXX
cloudflare_auth_key=CF_AUTH_KEY

# Get the current external IP address
ip=$(curl -s -X GET https://checkip.amazonaws.com)

echo "Current IP is $ip"

if host $dnsrecord 1.1.1.1 | grep "has address" | grep "$ip"; then
  echo "$dnsrecord is currently set to $ip; no changes needed"
  exit
fi

# get the zone id for the requested zone
zoneid=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones?name=$zone&status=active" \
  -H "X-Auth-Email: $cloudflare_auth_email" \
  -H "Authorization: Bearer $cloudflare_auth_key" \
  -H "Content-Type: application/json" | jq -r '{"result"}[] | .[0] | .id')

echo "Zoneid for $zone is $zoneid"

# get the dns record id
dnsrecordid=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones/$zoneid/dns_records?type=A&name=$dnsrecord" \
  -H "X-Auth-Email: $cloudflare_auth_email" \
  -H "Authorization: Bearer $cloudflare_auth_key" \
  -H "Content-Type: application/json" | jq -r '{"result"}[] | .[0] | .id')

echo "DNSrecordid for $dnsrecord is $dnsrecordid"

# update the record
curl -s -X PUT "https://api.cloudflare.com/client/v4/zones/$zoneid/dns_records/$dnsrecordid" \
  -H "X-Auth-Email: $cloudflare_auth_email" \
  -H "Authorization: Bearer $cloudflare_auth_key" \
  -H "Content-Type: application/json" \
  --data "{\"type\":\"A\",\"name\":\"$dnsrecord\",\"content\":\"$ip\",\"ttl\":1,\"proxied\":true}" | jq
