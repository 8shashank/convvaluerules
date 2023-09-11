from google.ads.googleads.client import GoogleAdsClient
client = GoogleAdsClient.load_from_storage("/Users/shank/repos/googleads/google-ads.yaml")
customer_id = "1574982141"
_DEFAULT_PAGE_SIZE = 10

conversion_value_rule_service = client.get_service("ConversionValueRuleService")

for i in range(1):
    conversion_value_rule_operation = client.get_type("ConversionValueRuleOperation")
    conversion_value_rule = conversion_value_rule_operation.create
    conversion_value_rule.action.value = 1
    conversion_value_rule.action.operation = client.enums.ValueRuleOperationEnum.ADD
    conversion_value_rule.device_condition.device_types  = [client.enums.ValueRuleDeviceTypeEnum.DESKTOP]

    # Execute the operation
    conversion_action_response = conversion_value_rule_service.mutate_conversion_value_rules(
            customer_id=customer_id, operations=[conversion_value_rule_operation],
        )

    # response = client.service.conversion_value_rule.mutate(
    #     customer_id="1574982141", operation=conversion_value_rule_operation
    # )

    # Print the result
    print(f"Created Conversion Value Rule: {conversion_action_response}")



# ga_service = client.get_service("GoogleAdsService")

# query = """
#     SELECT id FROM conversionvaluerule"""

# search_request = client.get_type("SearchGoogleAdsRequest")
# search_request.customer_id = customer_id
# search_request.query = query
# search_request.page_size = _DEFAULT_PAGE_SIZE

# results = ga_service.search(request=search_request)

# for row in results:
#     print(
#         f"Ad group with ID {row.ad_group.id} and name "
#         f'"{row.ad_group.name}" was found in campaign with '
#         f"ID {row.campaign.id}."
#     )



