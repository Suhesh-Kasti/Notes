---
category: knowledge
tags:
  - networking
platform: n/a
status: done
created: 2026-06-17
aliases:
  - About strategies for local traffic policy matching
---

Local traffic policies comprise a prioritized list of rules that match defined conditions and run specific actions, which you can assign to a virtual server that directs traffic accordingly
1. On the Main tab, click Local Traffic > Policies > Policy List .
2. Click Create.
3. In the Name field, type a unique name for the policy.
4. From the Strategy list, select a matching strategy.
5. For the Requires setting, select a protocol entry from the Available list, and move the entry to the Selected list using the Move button.
6. For the Controls setting, select a functional area or module from the Available list, and move the entry to the Selected list using the Move button.
7. Click Add.
8. In the Rule field, type a unique name for the rule.
9. Using the Conditions setting, configure the applicable options.
    1. From the Operand list, select an operand.
    2. From the Event list, select an event.
    3. From the Selector list, select the applicable setting.
    4. Select the Negate check box to reverse the policy conditions.
    5. From the Condition list, select a condition.
    6. Select the case sensitive check box to apply case sensitivity to the condition.
    7. In the Values field, type the text that applies to the condition and click Add.
        The condition text value appears in the Values list box.
    8. To the left, near the Missing setting, click Add.
        The configured condition appears in the Conditions list.
10. Using the Actions setting, configure the applicable options.
    1. From the Target list, select a target.
    2. From the Event list, select an event.
    3. From the Action list, select an action.
    4. From the Parameters list, select a type of parameter to apply.
    5. In the Parameters field, type the text that applies to the type of parameter and click Add.
    6. At the lower left, click Add.
11. Click Finished.

## About strategies for local traffic policy matching

Each BIG-IP® local traffic matching policy requires a matching strategy to determine the rule that applies if more than one rule matches.

The BIG-IP policies provide three policy matching strategies: a first-match, best-match, and all-match strategy. Each policy matching strategy prioritizes rules according to the rule's position within the Rules list.

Note: A rule without conditions becomes the default rule in a best-match or first-match strategy, when the rule is the last entry in the Rules list.

Table 1. Policy matching strategies

|Matching strategy|Description|
|---|---|
|First-match strategy|A first-match strategy starts the actions for the first rule in the Rules list that matches.|
|Best-match strategy|A best-match strategy selects and starts the actions of the rule in the Rules list with the best match, as determined by the following factors.<br><br>- The number of conditions and operands that match the rule.<br>- The length of the matched value for the rule.<br>- The priority of the operands for the rule.<br><br>Note: In a best-match strategy, when multiple rules match and specify an action, conflicting or otherwise, only the action of the best-match rule is implemented. A best-match rule can be the lowest ordinal, the highest priority, or the first rule that matches in the Rules list.|
|All-match strategy|An all-match strategy starts the actions for all rules in the Rules list that match.<br><br>Note: In an all-match strategy, when multiple rules match, but specify conflicting actions, only the action of the best-match rule is implemented. A best-match rule can be the lowest ordinal, the highest priority, or the first rule that matches in the Rules list.|

### Local traffic policy matching Requires profile settings

This table summarizes the profile settings that are required for local traffic policy matching.

|Requires Setting|Description|
|---|---|
|http|Specifies that the policy matching requires an HTTP profile.|
|ssl|Specifies that the policy matching requires a Client SSL profile.|
|tcp|Specifies that the policy matching requires a TCP profile.|

### Local traffic policy matching Controls settings

This table summarizes the controls settings that are required for local traffic policy matching.

|Controls Setting|Description|
|---|---|
|acceleration|Provides controls associated with acceleration functionality.|
|caching|Provides controls associated with caching functionality.|
|classification|Provides controls associated with classification.|
|compression|Provides controls associated with HTTP compression.|
|forwarding|Provides controls associated with forwarding functionality.|
|request-adaptation|Provides controls associated with request-adaptation functionality.|
|response-adaptation|Provides controls associated with response-adaptation functionality.|
|server-ssl|Provides controls associated with server-ssl functionality.|

## About rules for local traffic policy matching

BIG-IP® local traffic policy rules match defined conditions and start specific actions. You can create a policy with rules that are as simple or complex as necessary, based on the passing traffic. For example, a rule might simply determine that a client's browser is a Chrome browser that is not on an administrator network. Or a rule might determine that a request URL starts with /video, that the client is a mobile device, and that the client's subnet does not match 172.27.56.0/24.

## About conditions for local traffic policy matching

The conditions for a local traffic policy rule define the necessary criteria that must be met in order for the rule's actions to be applied. For example, a policy might include the following conditions, which, when met by a request, would allow the rule's specified actions to be applied.

|Condition|Setting|
|---|---|
|Operand|http-host|
|Event|request|
|Selector|all|
|Condition|equals|
|Values|www.siterequest.com|

### Local traffic policy matching Conditions operands

This table summarizes the operands for each condition used in policy matching.

| Operand         | Type          | Valid Events            | Selectors and Parameters                                                                                                                                                                                                                                                                | Description                                                           |
| --------------- | ------------- | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| client-ssl      | string/number | - request<br>- response | - cipher<br>- cipher-bits<br>- protocol                                                                                                                                                                                                                                                 | Requires a Client SSL profile for policy matching.                    |
| http-basic-auth | string        | - request               | - password<br>- username                                                                                                                                                                                                                                                                | Returns <username>: <password> or parts of it.                        |
| http-cookie     | string        | - request               | - all<br>    - name                                                                                                                                                                                                                                                                     | Returns the value of a particular cookie or cookie attribute.         |
| http-header     | string        | - request<br>- response | - all<br>    - name (required)                                                                                                                                                                                                                                                          | Returns the value of a particular header.                             |
| http-host       | string/number | - request               | - all<br>- host<br>- port                                                                                                                                                                                                                                                               | Provides all or part of the HTTP Host header.                         |
| http-method     | string        | - request               | - all                                                                                                                                                                                                                                                                                   | Provides the HTTP method.                                             |
| http-referer    | string/number | - request               | - all<br>- extension<br>- host<br>- path<br>- path-segment<br>    - index (required)<br>- port<br>- query-parameter<br>    - name (required)<br>- query-string<br>- scheme<br>- unnamed-query- parameter<br>    - index (required)                                                      | Provides all or part of the HTTP Referer header.                      |
| http-set-cookie | string        | - response              | - domain<br>    - name (required)<br>- expiry<br>    - name (required)<br>- path<br>    - name (required)<br>- value<br>    - name (required)<br>- version<br>    - name (required)                                                                                                     | Sets the selected setting of a particular cookie or cookie attribute. |
| http-status     | string/number | - response              | - all<br>- code<br>- text                                                                                                                                                                                                                                                               | Returns the HTTP status line or part of it.                           |
| http-uri        | string/number | - request               | - all<br>- extension<br>- host<br>- path<br>- path-segment<br>    - index (required)<br>- port<br>- query-parameter<br>    - name (required)<br>- query-string<br>- scheme<br>- unnamed-query- parameter<br>    - index (required)                                                      | Provides all or part of the request URI.                              |
| http-version    | string/number | - request<br>- response | - response<br>    - all<br>    - major<br>    - minor<br>    - protocol                                                                                                                                                                                                                 | Provides HTTP/1.1 a number.                                           |
| tcp             | number        | - request<br>- response | - address<br>    - internal true<br>    - local true<br>- mss<br>    - internal true<br>- port<br>    - internal true<br>    - local true<br>- route-domain<br>    - internal true<br>- rtt<br>    - internal true<br>- vlan<br>    - internal true<br>- vlan-id<br>    - internal true | Requires a TCP profile for policy matching.                           |

## About actions for a local traffic policy rule

The actions for a local traffic policy rule determine how traffic is handled. For example, actions for a rule could include the following ways of handling traffic.

- Blocking traffic
- Rewriting a URL
- Logging traffic
- Adding a specific header
- Redirecting traffic to a different pool member
- Selecting a specific Web Application policy

### Local traffic policy matching Actions operands

This table summarizes the actions associated with the conditions of the rule used in policy matching.

| Target          | Type          | Valid Events            | Action                                                                                                                                                                                 |
| --------------- | ------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| acceleration    | string/number | - request               | - disable<br>- enable                                                                                                                                                                  |
| cache           | string        | - request<br>- response | - disable<br>- enable<br>    - pin true                                                                                                                                                |
| compress        | string        | - request<br>- response | - disable<br>- enable                                                                                                                                                                  |
| decompress      | string        | - request<br>- response | - disable<br>- enable                                                                                                                                                                  |
| forward         | string        | - request               | - reset<br>- select<br>    - clone-pool<br>    - member<br>    - nexthop<br>    - node<br>    - pool<br>    - rateclass<br>    - snat<br>    - snatpool<br>    - vlan<br>    - vlan-id |
| http-cookie     | string        | - request               | - insert<br>    - name (required)<br>    - value (required)<br>- remove<br>    - name (required)                                                                                       |
| http-header     | string/number | - request<br>- response | - insert<br>    - name (required)<br>    - value (required)<br>- remove<br>    - name (required)<br>- replace<br>    - name (required)<br>    - value (required)                       |
| http-host       | string        | - request               | - replace<br>    - value                                                                                                                                                               |
| http-referer    | string        | - request               | - insert<br>    - value (required)<br>- remove<br>- replace<br>    - value                                                                                                             |
| http-reply      | string        | - request<br>- response | - redirect<br>    - location (required)                                                                                                                                                |
| http-set-cookie | string/number | - response              | - insert<br>    - name (required)<br>    - domain<br>    - path<br>    - value (required)<br>- remove<br>    - name (required)                                                         |
| http-uri        | string/number | - response              | - replace<br>    - path<br>    - query-string<br>    - value                                                                                                                           |
| log             | string/number | - request<br>- response | - write<br>    - message (required)                                                                                                                                                    |
| pem             | string/number | - request<br>- response | - classify<br>    - application<br>    - category<br>    - defer<br>    - protocol                                                                                                     |
| request-adapt   | string/number | - request<br>- response | - disable<br>- enable                                                                                                                                                                  |
| response-adapt  | string/number | - request<br>- response | - disable<br>- enable                                                                                                                                                                  |
| server-ssl      | string/number | - request               | - disable<br>- enable                                                                                                                                                                  |
| tcl             | string/number | - request<br>- response | - set-variable<br>    - name (required)<br>    - expression (required)                                                                                                                 |
| tcp-nagle       | string/number | - request               | - disable<br>- enable                                                                                                                                                                  |
