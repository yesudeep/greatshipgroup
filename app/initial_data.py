
from google.appengine.ext import db
from datetime import datetime

posts = (
    {
        'title': """Greatship (India) Ltd takes delivery of a modern Platform Supply Vessel""",
        'when_published': datetime(2007, 4, 17),
        'content': """
Greatship (India) Limited (GIL) a wholly owned subsidiary of The Great Eastern Shipping Co. Ltd. took delivery of a modern Platform Supply Vessel (PSV). The 2003 built PSV named "Greatship Diya" was contracted in May 23rd, 2006.

With the induction of "Greatship Diya", GIL has a current new building orderbook comprising 2 PSVs, 6 (80T) AHTSVs scheduled for delivery between H2CY 2007- H1CY 2009 and 1 secondhand PSV contracted for delivery during Q2 FY08.
        """
    },
    {
        'title': """Order for Two nos. 80 T AHTSVs placed""",
        'when_published': datetime(2007, 6, 27),
        'content': """
Greatship Global Offshore Services Pte.Ltd. , Singapore a wholly owned subsidiary of Greatship Holdings BV, Netherlands has signed a contract for 2 nos new building Anchor Handling Tug cum Supply Vessels (AHTSVs). Greatship Holdings BV, Netherlands is a wholly owned subsidiary of Greatship (India) Limited (GIL).

G E Shipping's wholly owned subsidiary GIL is pursuing business opportunities in the offshore oil field services business. G E Shipping has committed to invest in GIL around Rs.590 crores towards equity contribution of which around Rs. 305 crores has already been infused towards equity subscription at a premium of Rs.90 per share.

The 80 T - AHTSVs ordered with Colombo Dockyard Ltd. are scheduled to be delivered one each during Q4 FY 2008-09 and Q1 FY 2009-10. This brings the total new building order book of GIL and its subsidiaries at 10 Offshore Supply Vessels (2 PSVs and 8 AHTSVs) to be delivered over the next 2 years. Apart from this, a second hand modern PSV is scheduled to be delivered during Q2 FY 2007-08 while the 350 feet new building Jack Up rig ordered with Keppel is due for delivery during Q3 FY 2009-10.
        """
    },
    {
        'title': """New building order placed for 2 state of the art PSV's""",
        'when_published': datetime(2007, 7, 20),
        'content': """
Greatship Global Offshore Services Pte. Ltd, Singapore has signed a contract for 2 new building Multi Purpose Platform Supply & Support Vessels with Keppel Singmarine Pte. Ltd, Singapore. These vessels are expected to join the company's fleet in Q2FY 2009-10. The Multi Purpose Platform Supply & Support Vessels are of 4600+ dwt, fitted with DP-2 and have diesel electric propulsion. The vessels, which are also prepared for helideck and offshore crane, are larger and technologically more advanced than any PSV currently operational in the Indian waters.

Greatship Global Offshore Services Pte. Ltd is wholly owned by Greatship (India) Limited (GIL), which in turn is a wholly owned subsidiary of G E Shipping.

GIL and its subsidiaries already have a new building order book of 10 new building Offshore Supply Vessels (2 mid sized PSV's and 8 AHTSV's) and 1 new building 350 feet Jack up Rig.Apart from this, there is also 1 second hand modern PSV which is to be delivered in Q2 FY 2007-08.
        """
    },
    {
        'title': """New building order placed for 2 more state of the art PSV's""",
        'when_published': datetime(2007, 8, 6),
        'content': """
Greatship Global Offshore Services Pte. Ltd, Singapore has signed a contract for 2 more new building Multi Purpose Platform Supply & Support Vessels with Keppel Singmarine Pte. Ltd, Singapore. These vessels are expected to join the company's fleet in H2FY 2009-10. The Multi Purpose Platform Supply & Support Vessels, similar to the ones ordered in July this year, are of 4600+ dwt, fitted with DP-2 and have diesel electric propulsion. The vessels, which are also prepared for helideck and offshore crane, are larger and technologically more advanced than any PSV currently operating in Indian waters.

Greatship Global Offshore Services Pte. Ltd is wholly owned by Greatship (India) Limited (GIL), which in turn is a wholly owned subsidiary of G E Shipping. GIL and its subsidiaries already have a new building order book of 12 new building Offshore Supply Vessels and 1 new building 350 feet Jack up Rig. Apart from this, there is also 1 second hand modern PSV, which is to be delivered in Q2 FY 2007-08.
        """
    },
    {
        'title': """Greatship (India) Limited takes delivery of a modern Platform Supply Vessel""",
        'when_published': datetime(2007, 9, 26),
        'content': """
Greatship (India) Limited (GIL), a wholly owned subsidiary of Great Eastern Shipping Company Limited took delivery of a 2005 built modern Platform Supply Vessel (PSV). The PSV now named "Greatship Dipti" is a state of the art vessel of UT 755 LN design equipped with DP2 capabilities and was contracted by GIL in September 2006.

Greatship (India) Limited (GIL), a wholly owned subsidiary of Great Eastern Shipping Company Limited took delivery of a 2005 built modern Platform Supply Vessel (PSV). The PSV now named "Greatship Dipti" is a state of the art vessel of UT 755 LN design equipped with DP2 capabilities and was contracted by GIL in September 2006.
        """
    },
    {
        'title': """GREATSHIP FORAYS INTO HIGH END MULTI SUPPORT VESSELS (MSVs)""",
        'when_published': datetime(2007, 11, 30),
        'content': """
Greatship Global Offshore Services Pte. Ltd., the wholly owned subsidiary of Greatship (India) Limited (GIL), has announced the upgradation of the two vessels ordered on Mazagon Dock Limited to Multi Support Vessels (MSVs). As previously announced, the company had contracted two Multi Purpose Platform Supply & Support Vessels (MT6012 design) to be delivered in the third and fourth quarters of 2009-10. These vessels were designed for operating in deep waters (1000 - 3500 metres water depth), supplying and supporting complex exploration and production operations far away from shore.

Now, these vessels have been upgraded to MT6012 Mark II design. Each will be equipped with a 100 Ton active heave compensation offshore crane, a helideck, increased accommodation (100 pax), a moonpool (for diving and ROV services) and be prepared for FiFi 1 & 2. With these enhancements, the vessels will become part of an exclusive and limited global fleet of MSVs capable of multiple operations and outputs.

This upgradation has been done with the objective of tapping the burgeoning sub-sea construction markets, both globally as well as in India. MSVs play a critical role in new construction and in maintenance of various offshore assets and equipment, and will see increasing demand as the world moves further offshore (into deeper and distant waters) in search of new reserves of oil and gas. GIL currently own and operate three PSVs, two in India and one in the North Sea. GIL, along with its subsidiaries, also has an order book of sixteen vessels and one rig under construction - two PSVs in Norway, four AHTSVs in Sri Lanka, four AHTSVs and four MPSVs in Singapore, these two MSVs in India and a premium 350' jack up rig in Singapore.
        """
    },
    {
        'title': """GREATSHIP ORDERS TWO STATE-OF-THE-ART CONSTRUCTION SUPPORT VESSELS (MPSVs/ROV Support Vessels)""",
        'when_published': datetime(2007, 12, 18),
        'content': """
Greatship Global Offshore Services Pte. Ltd., the wholly owned subsidiary of Greatship (India) Limited (GIL), has placed an order for two state-of-the-art construction support vessels on Colombo Dockyard Limited. These MPSVs/ROV Support Vessels are due for delivery in January and May 2010.

These vessels are designed both for operating as advanced PSVs, with enhanced accommodation (50 pax), DP2 capability, as well as ROV Support Vessels, and are prepared for 50T Active Heave Compensated cranes, 50T A-frames and helidecks.

This order is in line with GIL's strategy of tapping the burgeoning sub-sea construction markets, both globally as well as in India.

GIL currently owns and operates three PSVs, two in India and one in the North Sea. GIL and its subsidiaries also have an order book of sixteen vessels and one rig under construction - two PSVs in Norway, four AHTSVs in Sri Lanka, four AHTSVs in Batam, four MPSVs in Singapore, two MSVs in India and a premium 350' jack up rig in Singapore.
        """
    },
    {
        'title': """Greatship (India) Limited takes delivery of an Anchor Handling Tug cum Supply Vessel (AHTSV)""",
        'when_published': datetime(2008, 1, 2),
        'content': """
Greatship (India) Limited (GIL), a wholly owned subsidiary of The Great Eastern Shipping Company Limited (GE Shipping) took delivery of new-built Anchor Handling Tug cum Supply Vessel (AHTSV). The AHTSV, named "Greatship Anjali", which was contracted by GIL in August 2006, is a DP2 vessel with bollard pull of 85 tons.

With the delivery of "Greatship Anjali", the company now has a fleet of 3 PSV's and 1 AHTSV in the water.

GIL along with its subsidiaries has a new building orderbook of 2 PSV's, 6 Multipurpose Platform Supply & Support Vessels, 2 MSVs, 7 AHTSV's and a 350 ft Jack up Rig.
        """
    },
    {
        'title': """Greatship (India) Limited takes delivery of its second Anchor Handling Tug cum Supply Vessel (AHTSV)""",
        'when_published': datetime(2008, 4, 8),
        'content': """
Greatship (India) Limited (GIL), a wholly owned subsidiary of The Great Eastern Shipping Company Limited (GE Shipping) took delivery of a new-built Anchor Handling Tug cum Supply Vessel (AHTSV). The AHTSV "Greatship Amrita", which was contracted by GIL in August 2006, is a DP2, FiFi 1 vessel with maximum bollard pull of 96 tons.

With the delivery of "Greatship Amrita", the company now has a fleet of 3 PSV's and 2 AHTSVs in the water.

GIL along with its subsidiaries has a new building orderbook of 2 PSV's, 6 Multipurpose Platform Supply & Support Vessels, 2 MSVs, 6 AHTSV's and a 350 ft Jack up Rig
        """
    },
    {
        'title': """GREATSHIP ORDERS TWO STATE-OF-THE-ART CONSTRUCTION SUPPORT VESSELS(MPSVs/ROV Support Vessels)""",
        'when_published': datetime(2008, 5, 2),
        'content': """
Greatship (India) Limited (GIL), a wholly owned subsidiary of The Great Eastern Shipping Co. Ltd. has placed an order for two state-of-the-art construction support vessels on Colombo Dockyard Limited. These MPSVs/ROV Support Vessels are due for delivery in September 2010 and January 2011.

These vessels are designed both for operating as advanced PSVs, with enhanced accommodation (50 pax), DP2 capability, as well as ROV Support Vessels, and are prepared for 50T Active Heave Compensated cranes, 50T A-frames and helidecks.

This order is in line with GIL's strategy of tapping the burgeoning sub-sea construction markets, both globally as well as in India.

GIL currently owns and operates three PSVs, two in India and one in the North Sea, and two AHTSV, one in India, and one in the Middle East. GIL and its subsidiaries also have an order book of sixteen vessels and one rig under construction - two PSVs in Norway, two AHTSVs in Sri Lanka, four AHTSVs in Batam, four MPSVs in Singapore, two MSVs in India, two MPSVs in Sri Lanka, and a premium 350' jack up rig in Singapore.        """
    },
    {
        'title': """New building order placed for 2 more state-of-the-art PSVs.""",
        'when_published': datetime(2007, 11, 6),
        'content': """
Greatship Global Offshore Services Pte. Ltd, Singapore has signed a contract for 2 new building Multi Purpose Platform Supply & Support Vessels with Mazagon Dock Ltd, Mumbai. These vessels are expected to join the company's fleet in H2 FY 2010.

The Multi Purpose Platform Supply & Support Vessels are of 4600+ dwt, fitted with DP-2 and have diesel electric propulsion. The vessels, which are also prepared for helideck and offshore crane, are larger and technologically more advanced than any PSV currently operational in the Indian waters.

Greatship Global Offshore Services Pte. Ltd is wholly owned by Greatship (India)Limited (GIL), which in turn is a wholly owned subsidiary of G E Shipping.

With this order, GIL and its subsidiaries have a new building order book of 16 new building Offshore Supply Vessels (2 mid sized PSV's, 8 AHTSV's, 6 MPSSV's) and 1 new building 350 feet Jack up Rig.
        """
    },
    {
        'title': """Greatship Orders Two STATE-OF-THE-ART Deep Water Anchor Handling, Towage & Supply Vessels""",
        'when_published': datetime(2008, 7, 24),
        'content': """
Greatship (India) Limited (GIL), a wholly owned subsidiary of The Great Eastern Shipping Co. Ltd. has placed an order for two state-of-the-art deep water 150 TBP Anchor Handling, Towage & Supply Vessels on Drydocks World Singapore. These vessels are due for delivery in January 2011 and March 2011. These vessels are designed for operating as efficient and safe towage, support and supply vessels in intermediate to deep waters, and have enhanced accommodation, DP2 capability, fire fighting equipment, and are SPS compliant in all respects.

This order is in line with GIL's strategy of tapping the burgeoning deep water offshore markets, both globally as well as in India.GIL currently owns and operates three PSVs, two in India and one in the North Sea, and two AHTSVs, one in South Africa, and one in the Middle East. GIL and its subsidiaries also have an order book of eighteen vessels and one rig under construction - two PSVs in Norway, two AHTSVs in Sri Lanka, four AHTSVs in Batam, four MPSVs in Singapore, two MSVs in India, four MPSVs in Sri Lanka, and a premium 350' jack up rig in Singapore.

With these two orders, the Greatship group, within the space of 27 months, has achieved the milestone of owning/ordering 25 modern, state-of-the-art offshore vessels. These vessels will provide a range of services to the offshore oilfield exploration and production domain, including supply, towage, support, safety standby, anchor handling, sub sea construction,diving, ROV deployment and support, etc. All Greatship's vessels are built to the highest standards of safety and operational efficiency, and conform to existing and envisaged IMO and Class rules, and are capable of operating in offshore waters across the world.
        """
    },
    {
        'title': """GREATSHIP TAKES DELIVERY OF PLATFORM SUPPORT VESSEL""",
        'when_published': datetime(2008, 9, 4),
        'content': """
Greatship (India) Limited (GIL), a wholly owned subsidiary of The Great Eastern Shipping Co. Ltd. has taken delivery of GREATSHIP DHRITI, a UT755LN Platform Support Vessel yesterday from Aker Yards, Norway.

Greatship Dhriti is a DP2, FiFi1 full service vessel built to exacting specifications, and capable of supporting offshore exploration and production globally. Immediately on delivery, the vessel will proceed to Mexico for a two year charter.

GIL currently owns and operates three PSVs, two in India and one in the North Sea, and two AHTSVs, one in South Africa, and one in the Middle East. GIL and its subsidiaries also have an order book of nineteen vessels and one rig under construction - one more PSV in Norway, two AHTSVs in Sri Lanka, four AHTSVs in Batam, four MPSVs in Singapore, two MSVs in India, four ROVSVs in Sri Lanka, two 150 TBP AHTSVs in Batam, and a premium 350' jack up rig in Singapore.

All Greatship's vessels are built to the highest standards of safety and operational efficiency, and conform to existing and envisaged IMO and Class rules, and are capable of operating in offshore waters across the world.
        """
    },
    {
        'title': """Greatship (India) Limited, India and DOF Subsea ASA, Norway announced the inking of their joint venture, in Mumbai today.""",
        'when_published': datetime(2008, 9, 8),
        'content': """
The joint venture, to be named GREATSHIP DOF SUBSEA PRIVATE LIMITED, will focus on subsea project opportunities in the Indian subcontinent.

DOF Subsea ASA is a world-wide supplier of subsea services with a presence in all the major offshore hubs in the world. Their core business is the execution of complex subsea operations down to depths of 4000 meters. The DOF Subsea group employs more than 800 skilled employees worldwide, 25 offshore vessels (8 under construction), 31 ROVs (10 more to be delivered), 1 AUV/UUV system and diving spreads. DOF Subsea currently owns the largest and most modern fleet of subsea construction vessels (including newbuildings) in the world

As a leading supplier of subsea services, DOF Subsea provides "solutions at any depth", including Project Management, Vessel operations, Subsea Engineering, ROV Intervention, Diving Intervention and Survey and Positioning.

For more information about DOF Subsea please visit www.dofsubsea.com

Greatship (India) Limited is a global offshore oilfield services provider, with six assets operating across the world and twenty under construction. Since their inception in 2006, the Greatship group has rapidly established itself as a supplier of state of the art assets and services to the offshore domain. The group's order book includes PSVs, mid-sized and large AHTSVs, MPSSVs, MSV, ROVSVs and a premium 350' jack up rig.

Mr. Steve Brown, CEO of DOF Subsea said "DOF Subsea is delighted to form this key joint venture with Greatship. Together with Greatship we are committed to building a substantial player in the offshore subsea projects market."

Mr. Ravi Sheth, MD of Greatship (India) Limited. said "We are excited about Greatship's joint venture with the world's leading subsea project company. We are very bullish on the prospects of offshore oilfield development off the East Coast of India and we expect the JV to be a leading player in the subsea construction domain."
        """
    },
    {
        'title': """Greatship Takes Delivery of Platfom Support Vessel""",
        'when_published': datetime(2008, 11, 22),
        'content': """
Greatship (India) Limited (GIL), a wholly owned subsidiary of The Great Eastern Shipping Co. Ltd. has taken delivery of GREATSHIP DHWANI, a UT755LN Platform Support Vessel, from Aker Yards, Norway.

Greatship Dhwani is a DP2, FiFi1 full service vessel built to exacting specifications, and capable of supporting offshore exploration and production globally. Immediately on delivery, the vessel will proceed to the North Sea.

GIL currently owns and operates four PSVs, two in India with ONGC and GSPC, one in the North Sea, and one in Mexico. GIL also owns and operates two AHTSVs, one in South Africa, and one in the Middle East.

GIL and its subsidiaries also have an order book of eighteen vessels and one rig under construction - two AHTSVs in Sri Lanka, four AHTSVs in Batam, four MPSVs in Singapore, two MSVs in India, four ROVSVs in Sri Lanka, two 150 TBP AHTSVs in Batam, and a premium 350' jack up rig in Singapore.

All Greatship's vessels are built to the highest standards of safety and operational efficiency, and conform to existing and envisaged IMO and Class rules, and are designed to operate in offshore waters across the world.
        """
    },
    {
        'title': """Greatship Subsidiary takes delivery of an 80T Anchor Handling Tug cum Supply Vessel (AHTSV)""",
        'when_published': datetime(2009, 2, 18),
        'content': """
Greatship Global Offshore Services Pte. Ltd. (GGOS), a Singapore incorporated subsidiary of Greatship (India) Limited (GIL), a wholly owned subsidiary of The Great Eastern Shipping Co. Ltd. has taken delivery of GREATSHIP ABHA, an 80T Anchor Handling Tug cum Supply Vessel, from Colombo Dockyard PLC, Sri Lanka. The vessel has been financed via a Sale and Lease Back Arrangement.

Greatship Abha is a DP2, FiFi1 full service vessel built to exacting specifications, and capable of supporting offshore exploration and production in various regions across the world. GIL currently owns and operates five PSVs, two in India with ONGC and GSPC, two in the North Sea, and one in Mexico. GIL also owns and operates two AHTSVs, one in South Africa, and one in the Middle East.

GIL and its subsidiaries also have an order book of seventeen vessels and one rig under construction - one AHTSV in Sri Lanka, four AHTSVs in Batam, four MPSVs in Singapore, two MSVs in India, four ROVSVs in Sri Lanka, two 150 TBP AHTSVs in Batam, and a premium 350' jack up rig in Singapore. All Greatship's vessels are built to the highest standards of safety and operational efficiency, and conform to existing and envisaged IMO and Class rules, and are designed to operate in offshore waters across the world.
        """
    },
    {
        'title': """Greatship takes delivery of an 80T anchor handling tug cum supply vessel (AHTSV)""",
        'when_published': datetime(2009, 4, 30),
        'content': """
Greatship (India) Limited (GIL), a wholly owned subsidiary of The Great Eastern Shipping Co. Ltd. has taken delivery of GREATSHIP ASMI, an 80T Anchor Handling Tug cum Supply Vessel. The vessel has been built at Labroy Shipbuilding and Engineering Pte Ltd (part of the Drydocks World Group) at their facilities in Batam, Indonesia.

Greatship Asmi is a DP2, FiFi1 full service vessel built to exacting specifications, and capable of supporting offshore exploration and production in various regions across the world. GIL and its subsidiaries currently own and / or operate six PSVs, five AHTSVs and one jack up rig.

GIL and its subsidiaries also have an order book of fifteen vessels and one rig under construction - one AHTSV in Sri Lanka, two AHTSVs in Batam, four MPSVs in Singapore, two MSVs in India, four ROVSVs in Sri Lanka, two 150 TBP AHTSVs in Batam, and a premium 350' jack up rig in Singapore. All Greatship's vessels are built to the highest standards of safety and operational efficiency, and conform to existing and envisaged IMO and Class rules, and are designed to operate in offshore waters across the world.
        """
    },
    {
        'title': """Greatship Subsidiary takes delivery of an 80T Anchor Handling Tug cum Supply Vessel (AHTSV)""",
        'when_published': datetime(2009, 6, 10),
        'content': """
Greatship Global Offshore Services Pte. Ltd. (GGOS), a Singapore incorporated subsidiary of Greatship (India) Limited (GIL), a wholly owned subsidiary of The Great Eastern Shipping Co. Ltd. has taken delivery of GREATSHIP ADITI, an 80T Anchor Handling Tug cum Supply Vessel, from Colombo Dockyard PLC, Sri Lanka. The vessel has been financed via a Sale and Lease Back Arrangement.

Greatship Aditi is a DP2, FiFi1 full service vessel built to exacting specifications, and capable of supporting offshore exploration and production in various regions across the world. GIL and its subsidiaries currently own and / or operate six PSVs, five AHTSVs and one jack up rig.

GIL and its subsidiaries also have an order book of fourteen vessels and one rig under construction - two AHTSVs in Batam, four MPSVs in Singapore, two MSVs in India, four ROVSVs in Sri Lanka, two 150 TBP AHTSVs in Batam, and a premium 350' jack up rig in Singapore. All Greatship's vessels are built to the highest standards of safety and operational efficiency, and conform to existing and envisaged IMO and Class rules, and are designed to operate in offshore waters across the world.
        """
    },
    {
        'title': """Greatship takes delivery of an 80T Anchor Handling Tug cum Supply Vessel (AHTSV)""",
        'when_published': datetime(2009, 6, 25),
        'content': """
Greatship (India) Limited (GIL), a wholly owned subsidiary of The Great Eastern Shipping Co. Ltd. has taken delivery of GREATSHIP AHALYA, an 80T Anchor Handling Tug cum Supply Vessel. The vessel has been built at Labroy Shipbuilding and Engineering Pte Ltd (part of the Drydocks World Group) at their facilities in Batam, Indonesia.

Greatship Ahalya is a DP2, FiFi1 full service vessel built to exacting specifications, and capable of supporting offshore exploration and production in various regions across the world. GIL and its subsidiaries currently own and / or operate six PSVs, six AHTSVs and one jack up rig.

GIL and its subsidiaries also have an order book of thirteen vessels and one rig under construction - one AHTSV in Batam, four MPSVs in Singapore, two MSVs in India, four ROVSVs in Sri Lanka, two 150 TBP AHTSVs in Batam, and a premium 350' jack up rig in Singapore. All Greatship's vessels are built to the highest standards of safety and operational efficiency, and conform to existing and envisaged IMO and Class rules, and are designed to operate in offshore waters across the world
        """
    },
    {
        'title': """Greatship takes delivery of an 80T Anchor Handling Tug cum Supply Vessel (AHTSV)""",
        'when_published': datetime(2009, 8, 27),
        'content': """
Greatship (India) Limited (GIL), a wholly owned subsidiary of The Great Eastern Shipping Co. Ltd. has taken delivery of GREATSHIP AARTI, an 80T Anchor Handling Tug cum Supply Vessel. The vessel has been built at Labroy Shipbuilding and Engineering Pte Ltd (part of the Drydocks World Group) at their facilities in Batam, Indonesia.

Greatship Aarti, is a DP2, FiFi1 full service vessel built to exacting specifications, and capable of supporting offshore exploration and production in various regions across the world. GIL and its subsidiaries currently own and / or operate six PSVs, seven AHTSVs and one jack up rig.

GIL and its subsidiaries also have an order book of twelve vessels and one rig under construction - four MPSVs in Singapore, two MSVs in India, four ROVSVs in Sri Lanka, two 150 TBP AHTSVs in Batam, and a premium 350' jack up rig in Singapore. All Greatship's vessels are built to the highest standards of safety and operational efficiency, and conform to existing and envisaged IMO and Class rules, and are designed to operate in offshore waters across the world.
        """
    },
    {
        'title': """Greatship Subsidiary takes delivery of a 350 foot jack-up rig.""",
        'when_published': datetime(2009, 10, 20),
        'content': """
Greatship Global Energy Services Pte. Ltd. (GGES), a Singapore incorporated subsidiary of Greatship (India) Limited (GIL), a wholly owned subsidiary of The Great Eastern Shipping Co. Ltd. has taken delivery of GREATDRILL CHITRA, a 350 FOOT Jack up Rig, from Keppel Fels yard, Singapore.

Greatdrill Chitra is a 350 foot, 15000 PSI, Mod V B Jack Up Rig, capable of drilling in most offshore waters across the world. She is a state of the art cyber rig, built with the latest in technology and systems.

Greatdrill Chitra has an employment contract with ONGC for a period of five years, and will work in the West Coast of India. She will join Greatdrill Chetna, currently in operation in the same region.

The delivery of Greatdrill Chitra is a significant milestone in Greatship's journey. In the short space of three and a half years, the Group has established itself as an offshore service provider of note, not just in one region, but across the world.

GIL and its subsidiaries currently own and / or operate six PSVs, eight AHTSVs and one jack up rig.

GIL and its subsidiaries also have an order book of twelve vessels - four MPSVs in Singapore, two MSVs in India, four ROVSVs in Sri Lanka, and two 150 TBP AHTSVs in Batam . All of Greatship's vessels are built to the highest standards of safety and operational efficiency, and conform to existing and envisaged IMO and Class rules, and are designed to operate in offshore waters across the world.
        """
    },
    {
        'title': """Greatship Subsidiary takes delivery of a Multipurpose Platform Supply and Support Vessel (MPSSV)""",
        'when_published': datetime(2009, 12, 23),
        'content': """
Greatship Global Offshore Services Pte. Ltd. (GGOS), a Singapore incorporated subsidiary of Greatship (India) Limited (GIL), a wholly owned subsidiary of The Great Eastern Shipping Co. Ltd. has taken delivery of GREATSHIP MAYA, a Multipurpose Platform Supply and Support Vessel, from Keppel Singmarine Pte. Ltd., Singapore.

Greatship Maya is a DP2, full service vessel built to exacting specifications, capable of supporting offshore exploration and production in various regions across the world and is one of the first vessels worldwide to be built complying with the new SPS Code 2008. With the delivery of Greatship Maya, GIL and its subsidiaries currently own and / or operate six PSVs, eight AHTSVs, two jack up rigs and one MPSSV.

GIL and its subsidiaries also have an order book of eleven vessels - three MPSSVs in Singapore, two MSVs in India, four ROVSVs in Sri Lanka and two 150 TBP AHTSVs in Batam . All of Greatship's vessels are built to the highest standards of safety and operational efficiency, and conform to existing and envisaged IMO and Class rules, and are designed to operate in offshore waters across the world
        """
    },
    {
        'title': """Greatship and Greatship's subsidiary contract to sell a Platform Supply Vessel (PSV) and a Platform/ROV Support Vessel (ROVSV), respectively.""",
        'when_published': datetime(2009, 12, 29),
        'content': """
Greatship (India) Limited (GIL), a wholly owned subsidiary of The Great Eastern Shipping Co. Ltd. has contracted to sell its Platform Supply Vessel "Greatship Diya". This 2003 built, 3350 dwt PSV is expected to be delivered to the buyers in Q1 FY11.

Greatship Global Offshore Services Pte. Ltd. (GGOS), a Singapore incorporated subsidiary of GIL, has also contracted to sell its Platform/ROV Support Vessel identified as Hull No. NC 0215 (tbn "Greatship Rekha") which is currently under construction. This 3000 dwt ROVSV is expected to be delivered to the buyers in Q4 FY10.

The current owned and/or operated fleet of GIL and its subsidiaries stands at six PSVs, eight AHTSVs, two jack up rigs and one MPSSV. The current order book of GIL and its subsidiaries comprises of eleven vessels - three MPSSVs in Singapore, two MSVs in India, four ROVSVs in Sri Lanka and two 150 TBP AHTSVs in Batam.
        """
    },   
)

def import_data():
    import_posts()

def import_posts():
    from models import Post
    save_posts = []
    for entry in posts:
        post = Post()
        post.title = unicode(entry['title'])
        post.content = entry['content']
        post.when_published = entry['when_published']
        post.is_published = True
        post.place = "Mumbai"
        post.path = post.format_post_path()
        post.content_html = post.rendered
        post.checksum = post.hash
        save_posts.append(post)
    db.put(save_posts)
