# META Platform major DNS failure Postmortem.
On 4th October, it was reported that the Meta platforms specifically Whatsapp was returning 'Make sure your computer has an active internet connection, error message. The issue was linked to the to BGP Border Gateway Protocal which helps one network find the best route to a different network leading to major DNS failure that affected the whole platform globally.

#Timeline
The error was realized on Tuesday 4th October 1000 hours (East Africa Time) when our Site Reliability Engineer, Mr Gichiah noticed that the BGP routes to Facebook had been dropped from the Internet for for Facebook’s ASN. This resulted in the Facebook domain being reported as being non existant and open for sale on Whois domain name lookup services and domain name registrars. Our engineers on call disconnected the master server web-01 for further system analysis and channelled all requests to client servers. The problem was solved by Tuesday 4th October 1300 hours (East Africa Time) 3 hours later.

#Root cause and resolution
The problem was as a result of a technical error that saw one of the junior staff accidentally withdraw all of facebooks Border Gateway Protocal routes from the internet which resulted in the Facebook domain disappearance from the internet. The domain was restored after paying a fee and the systems engineers worked hard to set up the domain and configure it inorder to bring operations back to normal within a short time frame.

#Measures against such problem in future
*Juniour Staff should work under the direct instruction of the senior engineers
-Limit access to important systems to experts 

