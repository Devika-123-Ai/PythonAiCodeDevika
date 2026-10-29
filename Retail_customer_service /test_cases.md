Basic manual test cases
TC ID	Test scenario	  Test data	            Expected result
TC01	Normal membership	200, normal, no	    $200
TC02	Basic membership	200, basic, no	    $190
TC03	Premium membership	200, premium,no	    $180
TC04	Valid coupon	200, normal, yes	    $180
TC05	Basic + coupon	200, basic, yes	        $170
TC06	Premium + coupon	200, premium, yes	$160
TC07	Cart below $100	99, normal, yes	        $99
TC08	Cart exactly $100	100, normal, yes	$90
TC09	Negative cart	-100	                Invalid cart total
TC10	Invalid membership	200, vip	        Invalid membership
TC11	Invalid coupon	200, basic, maybe	    Invalid coupon message
TC12	Invalid amount	abc	I                   nvalid cart total message
TC13	Uppercase membership	200, BASIC, no	$190
TC14	Membership with spaces	200, premium with spaces, no	$180
TC15	Zero cart	0, normal, no	                                $0