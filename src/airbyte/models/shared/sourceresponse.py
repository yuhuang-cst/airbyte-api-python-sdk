"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import source_aha as shared_source_aha
from ..shared import source_aircall as shared_source_aircall
from ..shared import source_airtable as shared_source_airtable
from ..shared import source_alloydb as shared_source_alloydb
from ..shared import source_amazon_ads as shared_source_amazon_ads
from ..shared import source_amazon_seller_partner as shared_source_amazon_seller_partner
from ..shared import source_amazon_sqs as shared_source_amazon_sqs
from ..shared import source_amplitude as shared_source_amplitude
from ..shared import source_apify_dataset as shared_source_apify_dataset
from ..shared import source_appfollow as shared_source_appfollow
from ..shared import source_asana as shared_source_asana
from ..shared import source_auth0 as shared_source_auth0
from ..shared import source_aws_cloudtrail as shared_source_aws_cloudtrail
from ..shared import source_azure_blob_storage as shared_source_azure_blob_storage
from ..shared import source_azure_table as shared_source_azure_table
from ..shared import source_bamboo_hr as shared_source_bamboo_hr
from ..shared import source_bigcommerce as shared_source_bigcommerce
from ..shared import source_bigquery as shared_source_bigquery
from ..shared import source_bing_ads as shared_source_bing_ads
from ..shared import source_braintree as shared_source_braintree
from ..shared import source_braze as shared_source_braze
from ..shared import source_chargebee as shared_source_chargebee
from ..shared import source_chartmogul as shared_source_chartmogul
from ..shared import source_clickhouse as shared_source_clickhouse
from ..shared import source_clickup_api as shared_source_clickup_api
from ..shared import source_clockify as shared_source_clockify
from ..shared import source_close_com as shared_source_close_com
from ..shared import source_coda as shared_source_coda
from ..shared import source_coin_api as shared_source_coin_api
from ..shared import source_coinmarketcap as shared_source_coinmarketcap
from ..shared import source_configcat as shared_source_configcat
from ..shared import source_confluence as shared_source_confluence
from ..shared import source_convex as shared_source_convex
from ..shared import source_datascope as shared_source_datascope
from ..shared import source_delighted as shared_source_delighted
from ..shared import source_dixa as shared_source_dixa
from ..shared import source_dockerhub as shared_source_dockerhub
from ..shared import source_dremio as shared_source_dremio
from ..shared import source_dynamodb as shared_source_dynamodb
from ..shared import source_e2e_test_cloud as shared_source_e2e_test_cloud
from ..shared import source_emailoctopus as shared_source_emailoctopus
from ..shared import source_exchange_rates as shared_source_exchange_rates
from ..shared import source_facebook_marketing as shared_source_facebook_marketing
from ..shared import source_facebook_pages as shared_source_facebook_pages
from ..shared import source_faker as shared_source_faker
from ..shared import source_fauna as shared_source_fauna
from ..shared import source_file_secure as shared_source_file_secure
from ..shared import source_firebolt as shared_source_firebolt
from ..shared import source_freshcaller as shared_source_freshcaller
from ..shared import source_freshdesk as shared_source_freshdesk
from ..shared import source_freshsales as shared_source_freshsales
from ..shared import source_gainsight_px as shared_source_gainsight_px
from ..shared import source_gcs as shared_source_gcs
from ..shared import source_getlago as shared_source_getlago
from ..shared import source_github as shared_source_github
from ..shared import source_gitlab as shared_source_gitlab
from ..shared import source_glassfrog as shared_source_glassfrog
from ..shared import source_gnews as shared_source_gnews
from ..shared import source_google_ads as shared_source_google_ads
from ..shared import source_google_analytics_data_api as shared_source_google_analytics_data_api
from ..shared import source_google_analytics_v4 as shared_source_google_analytics_v4
from ..shared import source_google_directory as shared_source_google_directory
from ..shared import source_google_pagespeed_insights as shared_source_google_pagespeed_insights
from ..shared import source_google_search_console as shared_source_google_search_console
from ..shared import source_google_sheets as shared_source_google_sheets
from ..shared import source_google_webfonts as shared_source_google_webfonts
from ..shared import source_google_workspace_admin_reports as shared_source_google_workspace_admin_reports
from ..shared import source_greenhouse as shared_source_greenhouse
from ..shared import source_gridly as shared_source_gridly
from ..shared import source_harvest as shared_source_harvest
from ..shared import source_hubplanner as shared_source_hubplanner
from ..shared import source_hubspot as shared_source_hubspot
from ..shared import source_insightly as shared_source_insightly
from ..shared import source_instagram as shared_source_instagram
from ..shared import source_instatus as shared_source_instatus
from ..shared import source_intercom as shared_source_intercom
from ..shared import source_ip2whois as shared_source_ip2whois
from ..shared import source_iterable as shared_source_iterable
from ..shared import source_jira as shared_source_jira
from ..shared import source_k6_cloud as shared_source_k6_cloud
from ..shared import source_klarna as shared_source_klarna
from ..shared import source_klaviyo as shared_source_klaviyo
from ..shared import source_kustomer_singer as shared_source_kustomer_singer
from ..shared import source_kyve as shared_source_kyve
from ..shared import source_launchdarkly as shared_source_launchdarkly
from ..shared import source_lemlist as shared_source_lemlist
from ..shared import source_lever_hiring as shared_source_lever_hiring
from ..shared import source_linkedin_ads as shared_source_linkedin_ads
from ..shared import source_linkedin_pages as shared_source_linkedin_pages
from ..shared import source_linnworks as shared_source_linnworks
from ..shared import source_lokalise as shared_source_lokalise
from ..shared import source_mailchimp as shared_source_mailchimp
from ..shared import source_mailgun as shared_source_mailgun
from ..shared import source_mailjet_sms as shared_source_mailjet_sms
from ..shared import source_marketo as shared_source_marketo
from ..shared import source_metabase as shared_source_metabase
from ..shared import source_microsoft_teams as shared_source_microsoft_teams
from ..shared import source_mixpanel as shared_source_mixpanel
from ..shared import source_monday as shared_source_monday
from ..shared import source_mongodb as shared_source_mongodb
from ..shared import source_mongodb_internal_poc as shared_source_mongodb_internal_poc
from ..shared import source_mssql as shared_source_mssql
from ..shared import source_my_hours as shared_source_my_hours
from ..shared import source_mysql as shared_source_mysql
from ..shared import source_netsuite as shared_source_netsuite
from ..shared import source_notion as shared_source_notion
from ..shared import source_nytimes as shared_source_nytimes
from ..shared import source_okta as shared_source_okta
from ..shared import source_omnisend as shared_source_omnisend
from ..shared import source_onesignal as shared_source_onesignal
from ..shared import source_oracle as shared_source_oracle
from ..shared import source_orb as shared_source_orb
from ..shared import source_orbit as shared_source_orbit
from ..shared import source_outbrain_amplify as shared_source_outbrain_amplify
from ..shared import source_outreach as shared_source_outreach
from ..shared import source_paypal_transaction as shared_source_paypal_transaction
from ..shared import source_paystack as shared_source_paystack
from ..shared import source_pendo as shared_source_pendo
from ..shared import source_persistiq as shared_source_persistiq
from ..shared import source_pexels_api as shared_source_pexels_api
from ..shared import source_pinterest as shared_source_pinterest
from ..shared import source_pipedrive as shared_source_pipedrive
from ..shared import source_pocket as shared_source_pocket
from ..shared import source_pokeapi as shared_source_pokeapi
from ..shared import source_polygon_stock_api as shared_source_polygon_stock_api
from ..shared import source_postgres as shared_source_postgres
from ..shared import source_posthog as shared_source_posthog
from ..shared import source_postmarkapp as shared_source_postmarkapp
from ..shared import source_prestashop as shared_source_prestashop
from ..shared import source_punk_api as shared_source_punk_api
from ..shared import source_pypi as shared_source_pypi
from ..shared import source_qualaroo as shared_source_qualaroo
from ..shared import source_quickbooks as shared_source_quickbooks
from ..shared import source_railz as shared_source_railz
from ..shared import source_recharge as shared_source_recharge
from ..shared import source_recreation as shared_source_recreation
from ..shared import source_recruitee as shared_source_recruitee
from ..shared import source_recurly as shared_source_recurly
from ..shared import source_redshift as shared_source_redshift
from ..shared import source_retently as shared_source_retently
from ..shared import source_rki_covid as shared_source_rki_covid
from ..shared import source_rss as shared_source_rss
from ..shared import source_s3 as shared_source_s3
from ..shared import source_salesforce as shared_source_salesforce
from ..shared import source_salesloft as shared_source_salesloft
from ..shared import source_sap_fieldglass as shared_source_sap_fieldglass
from ..shared import source_secoda as shared_source_secoda
from ..shared import source_sendgrid as shared_source_sendgrid
from ..shared import source_sendinblue as shared_source_sendinblue
from ..shared import source_senseforce as shared_source_senseforce
from ..shared import source_sentry as shared_source_sentry
from ..shared import source_sftp as shared_source_sftp
from ..shared import source_sftp_bulk as shared_source_sftp_bulk
from ..shared import source_shopify as shared_source_shopify
from ..shared import source_shortio as shared_source_shortio
from ..shared import source_slack as shared_source_slack
from ..shared import source_smaily as shared_source_smaily
from ..shared import source_smartengage as shared_source_smartengage
from ..shared import source_smartsheets as shared_source_smartsheets
from ..shared import source_snapchat_marketing as shared_source_snapchat_marketing
from ..shared import source_snowflake as shared_source_snowflake
from ..shared import source_sonar_cloud as shared_source_sonar_cloud
from ..shared import source_spacex_api as shared_source_spacex_api
from ..shared import source_square as shared_source_square
from ..shared import source_strava as shared_source_strava
from ..shared import source_stripe as shared_source_stripe
from ..shared import source_survey_sparrow as shared_source_survey_sparrow
from ..shared import source_surveymonkey as shared_source_surveymonkey
from ..shared import source_tempo as shared_source_tempo
from ..shared import source_the_guardian_api as shared_source_the_guardian_api
from ..shared import source_tiktok_marketing as shared_source_tiktok_marketing
from ..shared import source_todoist as shared_source_todoist
from ..shared import source_trello as shared_source_trello
from ..shared import source_trustpilot as shared_source_trustpilot
from ..shared import source_tvmaze_schedule as shared_source_tvmaze_schedule
from ..shared import source_twilio as shared_source_twilio
from ..shared import source_twilio_taskrouter as shared_source_twilio_taskrouter
from ..shared import source_twitter as shared_source_twitter
from ..shared import source_typeform as shared_source_typeform
from ..shared import source_us_census as shared_source_us_census
from ..shared import source_vantage as shared_source_vantage
from ..shared import source_webflow as shared_source_webflow
from ..shared import source_whisky_hunter as shared_source_whisky_hunter
from ..shared import source_wikipedia_pageviews as shared_source_wikipedia_pageviews
from ..shared import source_woocommerce as shared_source_woocommerce
from ..shared import source_xero as shared_source_xero
from ..shared import source_xkcd as shared_source_xkcd
from ..shared import source_yandex_metrica as shared_source_yandex_metrica
from ..shared import source_yotpo as shared_source_yotpo
from ..shared import source_younium as shared_source_younium
from ..shared import source_youtube_analytics as shared_source_youtube_analytics
from ..shared import source_zendesk_chat as shared_source_zendesk_chat
from ..shared import source_zendesk_sunshine as shared_source_zendesk_sunshine
from ..shared import source_zendesk_support as shared_source_zendesk_support
from ..shared import source_zendesk_talk as shared_source_zendesk_talk
from ..shared import source_zenloop as shared_source_zenloop
from ..shared import source_zoho_crm as shared_source_zoho_crm
from ..shared import source_zoom as shared_source_zoom
from ..shared import source_zuora as shared_source_zuora
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceResponse:
    r"""Provides details of a single source."""
    configuration: Union[shared_source_pokeapi.SourcePokeapi, shared_source_aha.SourceAha, shared_source_aircall.SourceAircall, shared_source_airtable.SourceAirtable, shared_source_alloydb.SourceAlloydb, shared_source_amazon_ads.SourceAmazonAds, shared_source_amazon_seller_partner.SourceAmazonSellerPartner, shared_source_amazon_sqs.SourceAmazonSqs, shared_source_amplitude.SourceAmplitude, shared_source_apify_dataset.SourceApifyDataset, shared_source_appfollow.SourceAppfollow, shared_source_asana.SourceAsana, shared_source_auth0.SourceAuth0, shared_source_aws_cloudtrail.SourceAwsCloudtrail, shared_source_azure_blob_storage.SourceAzureBlobStorage, shared_source_azure_table.SourceAzureTable, shared_source_bamboo_hr.SourceBambooHr, shared_source_bigcommerce.SourceBigcommerce, shared_source_bigquery.SourceBigquery, shared_source_bing_ads.SourceBingAds, shared_source_braintree.SourceBraintree, shared_source_braze.SourceBraze, shared_source_chargebee.SourceChargebee, shared_source_chartmogul.SourceChartmogul, shared_source_clickhouse.SourceClickhouse, shared_source_clickup_api.SourceClickupAPI, shared_source_clockify.SourceClockify, shared_source_close_com.SourceCloseCom, shared_source_coda.SourceCoda, shared_source_coin_api.SourceCoinAPI, shared_source_coinmarketcap.SourceCoinmarketcap, shared_source_configcat.SourceConfigcat, shared_source_confluence.SourceConfluence, shared_source_convex.SourceConvex, shared_source_datascope.SourceDatascope, shared_source_delighted.SourceDelighted, shared_source_dixa.SourceDixa, shared_source_dockerhub.SourceDockerhub, shared_source_dremio.SourceDremio, shared_source_dynamodb.SourceDynamodb, shared_source_e2e_test_cloud.SourceE2eTestCloud, shared_source_emailoctopus.SourceEmailoctopus, shared_source_exchange_rates.SourceExchangeRates, shared_source_facebook_marketing.SourceFacebookMarketing, shared_source_facebook_pages.SourceFacebookPages, shared_source_faker.SourceFaker, shared_source_fauna.SourceFauna, shared_source_file_secure.SourceFileSecure, shared_source_firebolt.SourceFirebolt, shared_source_freshcaller.SourceFreshcaller, shared_source_freshdesk.SourceFreshdesk, shared_source_freshsales.SourceFreshsales, shared_source_gainsight_px.SourceGainsightPx, shared_source_gcs.SourceGcs, shared_source_getlago.SourceGetlago, shared_source_github.SourceGithub, shared_source_gitlab.SourceGitlab, shared_source_glassfrog.SourceGlassfrog, shared_source_gnews.SourceGnews, shared_source_google_ads.SourceGoogleAds, shared_source_google_analytics_data_api.SourceGoogleAnalyticsDataAPI, shared_source_google_analytics_v4.SourceGoogleAnalyticsV4, shared_source_google_directory.SourceGoogleDirectory, shared_source_google_pagespeed_insights.SourceGooglePagespeedInsights, shared_source_google_search_console.SourceGoogleSearchConsole, shared_source_google_sheets.SourceGoogleSheets, shared_source_google_webfonts.SourceGoogleWebfonts, shared_source_google_workspace_admin_reports.SourceGoogleWorkspaceAdminReports, shared_source_greenhouse.SourceGreenhouse, shared_source_gridly.SourceGridly, shared_source_harvest.SourceHarvest, shared_source_hubplanner.SourceHubplanner, shared_source_hubspot.SourceHubspot, shared_source_insightly.SourceInsightly, shared_source_instagram.SourceInstagram, shared_source_instatus.SourceInstatus, shared_source_intercom.SourceIntercom, shared_source_ip2whois.SourceIp2whois, shared_source_iterable.SourceIterable, shared_source_jira.SourceJira, shared_source_k6_cloud.SourceK6Cloud, shared_source_klarna.SourceKlarna, shared_source_klaviyo.SourceKlaviyo, shared_source_kustomer_singer.SourceKustomerSinger, shared_source_kyve.SourceKyve, shared_source_launchdarkly.SourceLaunchdarkly, shared_source_lemlist.SourceLemlist, shared_source_lever_hiring.SourceLeverHiring, shared_source_linkedin_ads.SourceLinkedinAds, shared_source_linkedin_pages.SourceLinkedinPages, shared_source_linnworks.SourceLinnworks, shared_source_lokalise.SourceLokalise, shared_source_mailchimp.SourceMailchimp, shared_source_mailgun.SourceMailgun, shared_source_mailjet_sms.SourceMailjetSms, shared_source_marketo.SourceMarketo, shared_source_metabase.SourceMetabase, shared_source_microsoft_teams.SourceMicrosoftTeams, shared_source_mixpanel.SourceMixpanel, shared_source_monday.SourceMonday, shared_source_mongodb.SourceMongodb, shared_source_mongodb_internal_poc.SourceMongodbInternalPoc, shared_source_mssql.SourceMssql, shared_source_my_hours.SourceMyHours, shared_source_mysql.SourceMysql, shared_source_netsuite.SourceNetsuite, shared_source_notion.SourceNotion, shared_source_nytimes.SourceNytimes, shared_source_okta.SourceOkta, shared_source_omnisend.SourceOmnisend, shared_source_onesignal.SourceOnesignal, shared_source_oracle.SourceOracle, shared_source_orb.SourceOrb, shared_source_orbit.SourceOrbit, shared_source_outbrain_amplify.SourceOutbrainAmplify, shared_source_outreach.SourceOutreach, shared_source_paypal_transaction.SourcePaypalTransaction, shared_source_paystack.SourcePaystack, shared_source_pendo.SourcePendo, shared_source_persistiq.SourcePersistiq, shared_source_pexels_api.SourcePexelsAPI, shared_source_pinterest.SourcePinterest, shared_source_pipedrive.SourcePipedrive, shared_source_pocket.SourcePocket, shared_source_polygon_stock_api.SourcePolygonStockAPI, shared_source_postgres.SourcePostgres, shared_source_posthog.SourcePosthog, shared_source_postmarkapp.SourcePostmarkapp, shared_source_prestashop.SourcePrestashop, shared_source_punk_api.SourcePunkAPI, shared_source_pypi.SourcePypi, shared_source_qualaroo.SourceQualaroo, shared_source_quickbooks.SourceQuickbooks, shared_source_railz.SourceRailz, shared_source_recharge.SourceRecharge, shared_source_recreation.SourceRecreation, shared_source_recruitee.SourceRecruitee, shared_source_recurly.SourceRecurly, shared_source_redshift.SourceRedshift, shared_source_retently.SourceRetently, shared_source_rki_covid.SourceRkiCovid, shared_source_rss.SourceRss, shared_source_s3.SourceS3, shared_source_salesforce.SourceSalesforce, shared_source_salesloft.SourceSalesloft, shared_source_sap_fieldglass.SourceSapFieldglass, shared_source_secoda.SourceSecoda, shared_source_sendgrid.SourceSendgrid, shared_source_sendinblue.SourceSendinblue, shared_source_senseforce.SourceSenseforce, shared_source_sentry.SourceSentry, shared_source_sftp.SourceSftp, shared_source_sftp_bulk.SourceSftpBulk, shared_source_shopify.SourceShopify, shared_source_shortio.SourceShortio, shared_source_slack.SourceSlack, shared_source_smaily.SourceSmaily, shared_source_smartengage.SourceSmartengage, shared_source_smartsheets.SourceSmartsheets, shared_source_snapchat_marketing.SourceSnapchatMarketing, shared_source_snowflake.SourceSnowflake, shared_source_sonar_cloud.SourceSonarCloud, shared_source_spacex_api.SourceSpacexAPI, shared_source_square.SourceSquare, shared_source_strava.SourceStrava, shared_source_stripe.SourceStripe, shared_source_survey_sparrow.SourceSurveySparrow, shared_source_surveymonkey.SourceSurveymonkey, shared_source_tempo.SourceTempo, shared_source_the_guardian_api.SourceTheGuardianAPI, shared_source_tiktok_marketing.SourceTiktokMarketing, shared_source_todoist.SourceTodoist, shared_source_trello.SourceTrello, shared_source_trustpilot.SourceTrustpilot, shared_source_tvmaze_schedule.SourceTvmazeSchedule, shared_source_twilio.SourceTwilio, shared_source_twilio_taskrouter.SourceTwilioTaskrouter, shared_source_twitter.SourceTwitter, shared_source_typeform.SourceTypeform, shared_source_us_census.SourceUsCensus, shared_source_vantage.SourceVantage, shared_source_webflow.SourceWebflow, shared_source_whisky_hunter.SourceWhiskyHunter, shared_source_wikipedia_pageviews.SourceWikipediaPageviews, shared_source_woocommerce.SourceWoocommerce, shared_source_xero.SourceXero, shared_source_xkcd.SourceXkcd, shared_source_yandex_metrica.SourceYandexMetrica, shared_source_yotpo.SourceYotpo, shared_source_younium.SourceYounium, shared_source_youtube_analytics.SourceYoutubeAnalytics, shared_source_zendesk_chat.SourceZendeskChat, shared_source_zendesk_sunshine.SourceZendeskSunshine, shared_source_zendesk_support.SourceZendeskSupport, shared_source_zendesk_talk.SourceZendeskTalk, shared_source_zenloop.SourceZenloop, shared_source_zoho_crm.SourceZohoCrm, shared_source_zoom.SourceZoom, shared_source_zuora.SourceZuora] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuration') }})
    r"""The values required to configure the source."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    source_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId') }})
    source_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaceId') }})
    

