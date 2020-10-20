import pytest
from tap_peek.client import PeekClient

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
partner_id = os.getenv("PARTNER_ID")

def test_fetch_core_activities():
    client = PeekClient(api_key)
    response = client.fetch_core_activities(partner_id)

    included = response['included'][0]
    assert "attributes" in included
    assert "id" in included
    assert "type" in included

def test_fetch_core_addons():
    client = PeekClient(api_key)
    api_response = client.fetch_core_addons(partner_id)

    activity = api_response["activities"][0]

    assert "id" in activity
    assert "created_at" in activity
    assert "name" in activity
    assert "status" in activity
    assert "schedulable" in activity
    assert "currency" in activity
    assert "consumer_activity_status" in activity
    assert "minimum_booking_count" in activity
    assert "minimum_booking_prevents_purchase" in activity
    assert "partner_id" in activity

    if len(activity["tickets"]) > 0:
        assert "id" in activity["tickets"][0]
        assert "name" in activity["tickets"][0]
        assert "description" in activity["tickets"][0]
        assert "price" in activity["tickets"][0]
        assert "price_after_tax" in activity["tickets"][0]
        assert "status" in activity["tickets"][0]
    else:
        assert len(activity["tickets"]) == 0

def test_fetch_timeslots():
    client = PeekClient(api_key)
    api_response = client.fetch_timeslots()

    timeslot = api_response["timeslots"][0]

    assert "fid" in timeslot
    assert "time_series_id" in timeslot
    assert "activity_id" in timeslot
    assert "start" in timeslot
    assert "end" in timeslot
    assert "date" in timeslot
    assert "minute_length" in timeslot
    assert "resources_names" in timeslot
    assert "availability_status" in timeslot
    assert "availability_max_party_size" in timeslot
    assert "availability_total_capacity" in timeslot
    assert "availability_available_spots" in timeslot
    assert "availability_spots_taken" in timeslot
    assert "private_availability_code" in timeslot
    assert "time_series_type" in timeslot
    assert "is_freesale" in timeslot
    assert "is_fake" in timeslot
    assert "checked_in_count" in timeslot
    assert "manifest_notes" in timeslot

def test_fetch_transaction():
    client = PeekClient(api_key)
    api_response = client.fetch_transactions(partner_id)

    transaction = api_response["reporting/transaction_record"][0]

    assert "id" in transaction
    assert "created_at" in transaction
    assert "updated_at" in transaction
    assert "purchase_id" in transaction
    assert "purchase_display_gid" in transaction
    assert "parent_purchase_display_gid" in transaction
    assert "purchase_group_display_gid" in transaction
    assert "partner_id" in transaction
    assert "activity_id" in transaction
    assert "ticket_id" in transaction
    assert "display_source" in transaction
    assert "channel" in transaction
    assert "format" in transaction
    assert "payment_customer_method" in transaction
    assert "reseller_refid" in transaction
    assert "reseller_type" in transaction
    assert "reseller_description" in transaction
    assert "reseller_voucher_code" in transaction
    assert "reseller_group_description" in transaction
    assert "resell_payment_receiver" in transaction
    assert "payin_method" in transaction
    assert "context" in transaction
    assert "purchase_type" in transaction
    assert "currency" in transaction
    assert "commission_type" in transaction
    assert "activity_date" in transaction
    assert "activity_time_string" in transaction
    assert "predicted_payout_date" in transaction
    assert "actual_payout_date" in transaction
    assert "actual_payout_txn_refid" in transaction
    assert "payout_date" in transaction
    assert "redeem_date" in transaction
    assert "purchase_status" in transaction
    assert "checkin_date" in transaction
    assert "custom_status" in transaction
    assert "booking_status" in transaction
    assert "custom_source" in transaction
    assert "customer_first_name" in transaction
    assert "customer_last_name" in transaction
    assert "customer_email" in transaction
    assert "customer_zip" in transaction
    assert "customer_country" in transaction
    assert "activity_name" in transaction
    assert "ticket_description" in transaction
    assert "promo_code" in transaction
    assert "promo_code_refid" in transaction
    assert "salesforce_refid" in transaction
    assert "support_notes" in transaction
    assert "partner_notes" in transaction
    assert "purchase_date" in transaction
    assert "purchase_datetime" in transaction
    assert "tycoon_ledgerable_id" in transaction
    assert "activity_time_offset" in transaction
    assert "quantity" in transaction
    assert "currency_rate" in transaction
    assert "parent_activity_id" in transaction
    assert "promo_code_description" in transaction
    assert "parent_purchase_id" in transaction
    assert "simple_source" in transaction
    assert "booking_count" in transaction
    assert "guest_count" in transaction
    assert "item_count" in transaction
    assert "liability_count" in transaction
    assert "cc_description" in transaction
    assert "record_type" in transaction
    assert "collect_customer_payment_date" in transaction
    assert "partner_name" in transaction
    assert "voucher" in transaction
    assert "parent_activity_name" in transaction
    assert "daily_deal_name" in transaction
    assert "daily_deal_refid" in transaction
    assert "top_level_promo_code" in transaction
    assert "top_level_promo_code_refid" in transaction
    assert "peek_utm_campaign" in transaction
    assert "peek_utm_source" in transaction
    assert "peek_utm_medium" in transaction
    assert "peek_utm_content" in transaction
    assert "peek_utm_term" in transaction
    assert "peek_utm_first_seen" in transaction
    assert "widget_utm_campaign" in transaction
    assert "widget_utm_source" in transaction
    assert "widget_utm_medium" in transaction
    assert "widget_utm_content" in transaction
    assert "widget_utm_term" in transaction
    assert "widget_utm_first_seen" in transaction
    assert "widget_configuration_id" in transaction
    assert "bundle_item_id" in transaction
    assert "bundle_id" in transaction
    assert "bundle_primary_activity_id" in transaction
    assert "bundle_primary_activity_name" in transaction
    assert "is_bundle_primary_activity" in transaction
    assert "refund_policy_id" in transaction
    assert "refund_policy_name" in transaction
    assert "sequential_id" in transaction
    assert "sequential_scoped_id" in transaction
    assert "user_refid" in transaction
    assert "user_type" in transaction
    assert "top_level_user_refid" in transaction
    assert "top_level_user_type" in transaction
    assert "customer_price" in transaction
    assert "customer_discounts" in transaction
    assert "customer_fees_total" in transaction
    assert "customer_total" in transaction
    assert "partner_price" in transaction
    assert "partner_discounts" in transaction
    assert "partner_fees_total" in transaction
    assert "partner_taxes_perc_total" in transaction
    assert "partner_taxes_flat_total" in transaction
    assert "customer_peek_fees" in transaction
    assert "customer_peek_commission" in transaction
    assert "customer_peek_discounts" in transaction
    assert "customer_cc_fees_sum" in transaction
    assert "total_charges_to_customer" in transaction
    assert "peek_fee_paid_partner" in transaction
    assert "peek_com_paid_partner" in transaction
    assert "peek_cc_fee_paid_partner" in transaction
    assert "payment_to_partner" in transaction
    assert "price_resell_commission" in transaction
    assert "peek_net_revenue" in transaction
    assert "peek_cc_deficit" in transaction
    assert "partners_customer_fees_total" in transaction
    assert "peeks_customer_fees_total" in transaction
    assert "peeks_customer_fees_from_peek_commission" in transaction
    assert "peeks_customer_fees_from_peek_ticket_fee" in transaction
    assert "partner_net" in transaction
    assert "total_partner_fees" in transaction
    assert "total_peek_fees" in transaction
    assert "total_cc_fees" in transaction
    assert "total_retail_tax" in transaction
    assert "total_city_tax" in transaction
    assert "total_state_tax" in transaction
    assert "total_food_and_beverage_tax" in transaction
    assert "total_other_tax" in transaction
    assert "additional_partner_fee" in transaction
    assert "price_partner_fee" in transaction
    assert "price_post_discount_retail" in transaction
    assert "price_retail" in transaction
    assert "peeks_customer_fees_from_cc_fees" in transaction
    assert "payment_to_partner_no_cc" in transaction
    assert "partner_total_value" in transaction
    assert "total_peek_commission" in transaction
    assert "final_peek_net" in transaction
    assert "payment_to_partner_with_cc" in transaction
    assert "total_tax_value" in transaction
    assert "post_discount_retail_tax" in transaction
    assert "post_discount_food_and_beverage_tax" in transaction
    assert "post_discount_city_tax" in transaction
    assert "post_discount_state_tax" in transaction
    assert "post_discount_other_tax" in transaction
    assert "partner_revenue" in transaction
    assert "customer_price_usd" in transaction
    assert "customer_discounts_usd" in transaction
    assert "customer_fees_total_usd" in transaction
    assert "customer_total_usd" in transaction
    assert "partner_price_usd" in transaction
    assert "partner_discounts_usd" in transaction
    assert "partner_fees_total_usd" in transaction
    assert "partner_taxes_perc_total_usd" in transaction
    assert "partner_taxes_flat_total_usd" in transaction
    assert "customer_peek_fees_usd" in transaction
    assert "customer_peek_commission_usd" in transaction
    assert "customer_peek_discounts_usd" in transaction
    assert "customer_cc_fees_sum_usd" in transaction
    assert "total_charges_to_customer_usd" in transaction
    assert "peek_fee_paid_partner_usd" in transaction
    assert "peek_com_paid_partner_usd" in transaction
    assert "peek_cc_fee_paid_partner_usd" in transaction
    assert "payment_to_partner_usd" in transaction
    assert "price_resell_commission_usd" in transaction
    assert "peek_net_revenue_usd" in transaction
    assert "peek_cc_deficit_usd" in transaction
    assert "partners_customer_fees_total_usd" in transaction
    assert "peeks_customer_fees_total_usd" in transaction
    assert "peeks_customer_fees_from_peek_commission_usd" in transaction
    assert "peeks_customer_fees_from_peek_ticket_fee_usd" in transaction
    assert "partner_net_usd" in transaction
    assert "total_partner_fees_usd" in transaction
    assert "total_peek_fees_usd" in transaction
    assert "total_cc_fees_usd" in transaction
    assert "total_retail_tax_usd" in transaction
    assert "total_city_tax_usd" in transaction
    assert "total_state_tax_usd" in transaction
    assert "total_food_and_beverage_tax_usd" in transaction
    assert "total_other_tax_usd" in transaction
    assert "additional_partner_fee_usd" in transaction
    assert "price_partner_fee_usd" in transaction
    assert "price_post_discount_retail_usd" in transaction
    assert "price_retail_usd" in transaction
    assert "peeks_customer_fees_from_cc_fees_usd" in transaction
    assert "payment_to_partner_no_cc_usd" in transaction
    assert "partner_total_value_usd" in transaction
    assert "total_peek_commission_usd" in transaction
    assert "final_peek_net_usd" in transaction
    assert "payment_to_partner_with_cc_usd" in transaction
    assert "total_tax_value_usd" in transaction
    assert "post_discount_retail_tax_usd" in transaction
    assert "post_discount_food_and_beverage_tax_usd" in transaction
    assert "post_discount_city_tax_usd" in transaction
    assert "post_discount_state_tax_usd" in transaction
    assert "post_discount_other_tax_usd" in transaction
    assert "partner_revenue_usd" in transaction
    assert "purchase_flat_cc_fee" in transaction
    assert "purchase_flat_cc_fee_usd" in transaction
    assert "cc_fee_percentage" in transaction
    assert "convenience_fee" in transaction
