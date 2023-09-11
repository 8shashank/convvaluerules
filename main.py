from google.ads.googleads.client import GoogleAdsClient
import yaml

client = GoogleAdsClient.load_from_storage("/Users/shank/repos/googleads/google-ads.yaml")

# Load the account info from config file
userConfig = None
with open("user-config.yaml") as configFile:
    userConfig = yaml.safe_load(configFile)
customer_id = userConfig['customerId']

# Create new conversino value rules
conversion_value_rule_service = client.get_service("ConversionValueRuleService")

for i in range(5):
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
# _DEFAULT_PAGE_SIZE = 10

# query = """
#     SELECT id FROM conversionvaluerule"""

# search_request = client.get_type("SearchGoogleAdsRequest")
# search_request.customer_id = customer_id
# search_request.query = query
# search_request.page_size = _DEFAULT_PAGE_SIZE

# results = ga_service.search(request=search_request)

