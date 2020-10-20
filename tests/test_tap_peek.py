import vcr
import pytest
import pytest_vcr
from tap_peek.peek import *


@pytest.mark.vcr()
def test_fetch_core_activities():
    api_response = fetch_core_activities()

    first_response = api_response[0]

    assert "id" in first_response
    assert "name" in first_response["attributes"]
    assert "legacy-id" in first_response["attributes"]
    assert "info-to-know" in first_response["attributes"]
    assert "info-to-bring" in first_response["attributes"]
    assert "info-meeting-location" in first_response["attributes"]
    assert "info-included" in first_response["attributes"]
    assert "image-url" in first_response["attributes"]
    assert "description" in first_response["attributes"]


@pytest.mark.vcr()
def test_fetch_core_addons():
    api_response = fetch_core_addons()

    first_response = api_response["activities"][0]

    assert "id" in first_response
    assert "created_at" in first_response
    assert "name" in first_response
    assert "status" in first_response
    assert "schedulable" in first_response
    assert "currency" in first_response
    assert "consumer_activity_status" in first_response
    assert "minimum_booking_count" in first_response
    assert "minimum_booking_prevents_purchase" in first_response
    assert "partner_id" in first_response

    if len(first_response["tickets"]) > 0:
        assert "id" in first_response["tickets"][0]
        assert "name" in first_response["tickets"][0]
        assert "description" in first_response["tickets"][0]
        assert "price" in first_response["tickets"][0]
        assert "price_after_tax" in first_response["tickets"][0]
        assert "status" in first_response["tickets"][0]
    else:
        assert len(first_response["tickets"]) == 0


@pytest.mark.vcr()
def test_fetch_timeslots():
    api_response = fetch_timeslots()

    first_response = api_response["timeslots"][0]

    assert "fid" in first_response
    assert "time_series_id" in first_response
    assert "activity_id" in first_response
    assert "start" in first_response
    assert "end" in first_response
    assert "date" in first_response
    assert "minute_length" in first_response
    assert "resources_names" in first_response
    assert "availability_status" in first_response
    assert "availability_max_party_size" in first_response
    assert "availability_total_capacity" in first_response
    assert "availability_available_spots" in first_response
    assert "availability_spots_taken" in first_response
    assert "private_availability_code" in first_response
    assert "time_series_type" in first_response
    assert "is_freesale" in first_response
    assert "is_fake" in first_response
    assert "checked_in_count" in first_response
    assert "manifest_notes" in first_response


@pytest.mark.vcr()
def test_fetch_transaction():
    api_response = fetch_transactions()

    first_response = api_response["reporting/transaction_record"][0]

    assert "id" in first_response
    assert "created_at" in first_response
    assert "updated_at" in first_response
    assert "purchase_id" in first_response
    assert "purchase_display_gid" in first_response
    assert "parent_purchase_display_gid" in first_response
    assert "purchase_group_display_gid" in first_response
    assert "partner_id" in first_response
    assert "activity_id" in first_response
    assert "ticket_id" in first_response
    assert "display_source" in first_response
    assert "channel" in first_response
    assert "format" in first_response
    assert "payment_customer_method" in first_response
    assert "reseller_refid" in first_response
    assert "reseller_type" in first_response
    assert "reseller_description" in first_response
    assert "reseller_voucher_code" in first_response
    assert "reseller_group_description" in first_response
    assert "resell_payment_receiver" in first_response
    assert "payin_method" in first_response
    assert "context" in first_response
    assert "purchase_type" in first_response
    assert "currency" in first_response
    assert "commission_type" in first_response
    assert "activity_date" in first_response
    assert "activity_time_string" in first_response
    assert "predicted_payout_date" in first_response
    assert "actual_payout_date" in first_response
    assert "actual_payout_txn_refid" in first_response
    assert "payout_date" in first_response
    assert "redeem_date" in first_response
    assert "purchase_status" in first_response
    assert "checkin_date" in first_response
    assert "custom_status" in first_response
    assert "booking_status" in first_response
    assert "custom_source" in first_response
    assert "customer_first_name" in first_response
    assert "customer_last_name" in first_response
    assert "customer_email" in first_response
    assert "customer_zip" in first_response
    assert "customer_country" in first_response
    assert "activity_name" in first_response
    assert "ticket_description" in first_response
    assert "promo_code" in first_response
    assert "promo_code_refid" in first_response
    assert "salesforce_refid" in first_response
    assert "support_notes" in first_response
    assert "partner_notes" in first_response
    assert "purchase_date" in first_response
    assert "purchase_datetime" in first_response
    assert "tycoon_ledgerable_id" in first_response
    assert "activity_time_offset" in first_response
    assert "quantity" in first_response
    assert "currency_rate" in first_response
    assert "parent_activity_id" in first_response
    assert "promo_code_description" in first_response
    assert "parent_purchase_id" in first_response
    assert "simple_source" in first_response
    assert "booking_count" in first_response
    assert "guest_count" in first_response
    assert "item_count" in first_response
    assert "liability_count" in first_response
    assert "cc_description" in first_response
    assert "record_type" in first_response
    assert "collect_customer_payment_date" in first_response
    assert "partner_name" in first_response
    assert "voucher" in first_response
    assert "parent_activity_name" in first_response
    assert "daily_deal_name" in first_response
    assert "daily_deal_refid" in first_response
    assert "top_level_promo_code" in first_response
    assert "top_level_promo_code_refid" in first_response
    assert "peek_utm_campaign" in first_response
    assert "peek_utm_source" in first_response
    assert "peek_utm_medium" in first_response
    assert "peek_utm_content" in first_response
    assert "peek_utm_term" in first_response
    assert "peek_utm_first_seen" in first_response
    assert "widget_utm_campaign" in first_response
    assert "widget_utm_source" in first_response
    assert "widget_utm_medium" in first_response
    assert "widget_utm_content" in first_response
    assert "widget_utm_term" in first_response
    assert "widget_utm_first_seen" in first_response
    assert "widget_configuration_id" in first_response
    assert "bundle_item_id" in first_response
    assert "bundle_id" in first_response
    assert "bundle_primary_activity_id" in first_response
    assert "bundle_primary_activity_name" in first_response
    assert "is_bundle_primary_activity" in first_response
    assert "refund_policy_id" in first_response
    assert "refund_policy_name" in first_response
    assert "sequential_id" in first_response
    assert "sequential_scoped_id" in first_response
    assert "user_refid" in first_response
    assert "user_type" in first_response
    assert "top_level_user_refid" in first_response
    assert "top_level_user_type" in first_response
    assert "customer_price" in first_response
    assert "customer_discounts" in first_response
    assert "customer_fees_total" in first_response
    assert "customer_total" in first_response
    assert "partner_price" in first_response
    assert "partner_discounts" in first_response
    assert "partner_fees_total" in first_response
    assert "partner_taxes_perc_total" in first_response
    assert "partner_taxes_flat_total" in first_response
    assert "customer_peek_fees" in first_response
    assert "customer_peek_commission" in first_response
    assert "customer_peek_discounts" in first_response
    assert "customer_cc_fees_sum" in first_response
    assert "total_charges_to_customer" in first_response
    assert "peek_fee_paid_partner" in first_response
    assert "peek_com_paid_partner" in first_response
    assert "peek_cc_fee_paid_partner" in first_response
    assert "payment_to_partner" in first_response
    assert "price_resell_commission" in first_response
    assert "peek_net_revenue" in first_response
    assert "peek_cc_deficit" in first_response
    assert "partners_customer_fees_total" in first_response
    assert "peeks_customer_fees_total" in first_response
    assert "peeks_customer_fees_from_peek_commission" in first_response
    assert "peeks_customer_fees_from_peek_ticket_fee" in first_response
    assert "partner_net" in first_response
    assert "total_partner_fees" in first_response
    assert "total_peek_fees" in first_response
    assert "total_cc_fees" in first_response
    assert "total_retail_tax" in first_response
    assert "total_city_tax" in first_response
    assert "total_state_tax" in first_response
    assert "total_food_and_beverage_tax" in first_response
    assert "total_other_tax" in first_response
    assert "additional_partner_fee" in first_response
    assert "price_partner_fee" in first_response
    assert "price_post_discount_retail" in first_response
    assert "price_retail" in first_response
    assert "peeks_customer_fees_from_cc_fees" in first_response
    assert "payment_to_partner_no_cc" in first_response
    assert "partner_total_value" in first_response
    assert "total_peek_commission" in first_response
    assert "final_peek_net" in first_response
    assert "payment_to_partner_with_cc" in first_response
    assert "total_tax_value" in first_response
    assert "post_discount_retail_tax" in first_response
    assert "post_discount_food_and_beverage_tax" in first_response
    assert "post_discount_city_tax" in first_response
    assert "post_discount_state_tax" in first_response
    assert "post_discount_other_tax" in first_response
    assert "partner_revenue" in first_response
    assert "customer_price_usd" in first_response
    assert "customer_discounts_usd" in first_response
    assert "customer_fees_total_usd" in first_response
    assert "customer_total_usd" in first_response
    assert "partner_price_usd" in first_response
    assert "partner_discounts_usd" in first_response
    assert "partner_fees_total_usd" in first_response
    assert "partner_taxes_perc_total_usd" in first_response
    assert "partner_taxes_flat_total_usd" in first_response
    assert "customer_peek_fees_usd" in first_response
    assert "customer_peek_commission_usd" in first_response
    assert "customer_peek_discounts_usd" in first_response
    assert "customer_cc_fees_sum_usd" in first_response
    assert "total_charges_to_customer_usd" in first_response
    assert "peek_fee_paid_partner_usd" in first_response
    assert "peek_com_paid_partner_usd" in first_response
    assert "peek_cc_fee_paid_partner_usd" in first_response
    assert "payment_to_partner_usd" in first_response
    assert "price_resell_commission_usd" in first_response
    assert "peek_net_revenue_usd" in first_response
    assert "peek_cc_deficit_usd" in first_response
    assert "partners_customer_fees_total_usd" in first_response
    assert "peeks_customer_fees_total_usd" in first_response
    assert "peeks_customer_fees_from_peek_commission_usd" in first_response
    assert "peeks_customer_fees_from_peek_ticket_fee_usd" in first_response
    assert "partner_net_usd" in first_response
    assert "total_partner_fees_usd" in first_response
    assert "total_peek_fees_usd" in first_response
    assert "total_cc_fees_usd" in first_response
    assert "total_retail_tax_usd" in first_response
    assert "total_city_tax_usd" in first_response
    assert "total_state_tax_usd" in first_response
    assert "total_food_and_beverage_tax_usd" in first_response
    assert "total_other_tax_usd" in first_response
    assert "additional_partner_fee_usd" in first_response
    assert "price_partner_fee_usd" in first_response
    assert "price_post_discount_retail_usd" in first_response
    assert "price_retail_usd" in first_response
    assert "peeks_customer_fees_from_cc_fees_usd" in first_response
    assert "payment_to_partner_no_cc_usd" in first_response
    assert "partner_total_value_usd" in first_response
    assert "total_peek_commission_usd" in first_response
    assert "final_peek_net_usd" in first_response
    assert "payment_to_partner_with_cc_usd" in first_response
    assert "total_tax_value_usd" in first_response
    assert "post_discount_retail_tax_usd" in first_response
    assert "post_discount_food_and_beverage_tax_usd" in first_response
    assert "post_discount_city_tax_usd" in first_response
    assert "post_discount_state_tax_usd" in first_response
    assert "post_discount_other_tax_usd" in first_response
    assert "partner_revenue_usd" in first_response
    assert "purchase_flat_cc_fee" in first_response
    assert "purchase_flat_cc_fee_usd" in first_response
    assert "cc_fee_percentage" in first_response
    assert "convenience_fee" in first_response
