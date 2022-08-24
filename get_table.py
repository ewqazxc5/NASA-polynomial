from code import get_Cp_parameter
import csv

with open('coefficients.csv','a',newline='') as w:
        writer=csv.writer(w,delimiter=',')
    
        writer.writerow(['name','x^6','x^5','x^4','x^3','x^2','x^1','constant'])


with open('Cp0.csv','a',newline='') as w:
        writer=csv.writer(w,delimiter=',')
    
        writer.writerow(['name','3.00000e+02', '5.00000e+02',   '7.00000e+02',   '1.00000e+03',   '1.50000e+03',   '2.00000e+03'  , '3.00000e+03',   '4.00000e+03',   '5.00000e+03',   '6.00000e+03','variance'])




#H2 fit well
get_Cp_parameter(4,0.5,0.5,2)


#Li2  not fit
get_Cp_parameter(5,1.5,1.5,1)


#B2 little difference
get_Cp_parameter(6,1.5,1.5,2)

#C2  similar trend, have difference
get_Cp_parameter(7,0,0,2)

#N2 not bad
get_Cp_parameter(8,1,1,2)

#O2 fit well
get_Cp_parameter(9,0,0,2)

#F2 not good
get_Cp_parameter(10,0.5,0.5,2)

#Na2 not good
get_Cp_parameter(11,1.5,1.5,1)

#mg2
get_Cp_parameter(12,0,0,1)

#Al2
get_Cp_parameter(13,2.5,2.5,1)

#Si2
get_Cp_parameter(14,0,0,1)

#P2
get_Cp_parameter(15,0.5,0.5,2)
#S2
get_Cp_parameter(16,0,0,2)
#Cl2
get_Cp_parameter(17,1.5,1.5,1) 
#K2
get_Cp_parameter(18,1.5,1.5,2)
#Cu2
get_Cp_parameter(19,1.5,1.5,1)
#As2
get_Cp_parameter(20,1.5,1.5,1)
#Se2
get_Cp_parameter(21,0,0,1)
#Sb2
get_Cp_parameter(22,2.5,2.5,1)
#Te2
get_Cp_parameter(23,0,0,1)
#I2
get_Cp_parameter(24,2.5,2.5,2)
#Cs2
get_Cp_parameter(25,3.5,3.5,1)
#H2+
get_Cp_parameter(26,0.5,0.5,1)
#He2+
get_Cp_parameter(27,0,0,1)
# C2+
get_Cp_parameter(28,0,0,1)
#N2+
get_Cp_parameter(29,1,1,1)
#O2+
get_Cp_parameter(30,0,0,1)
#Ne2+
get_Cp_parameter(31,0,0,1)
#P2+
get_Cp_parameter(32,0.5,0.5,1)
#S2+
get_Cp_parameter(33,0,0,1)
#H2-
get_Cp_parameter(34,0.5,0.5,1)
#C2-
get_Cp_parameter(35,0,0,1)
#LiH
get_Cp_parameter(36,1.5,0.5,1)
#BeH 
get_Cp_parameter(37,1.5,0.5,1)
#BH
get_Cp_parameter(38,1.5,0.5,2)
#CH
get_Cp_parameter(39,0,0.5,2)
#NH
get_Cp_parameter(40,1,0.5,2)
#OH
get_Cp_parameter(41,0,0.5,2)
#HF
get_Cp_parameter(42,0.5,0.5,2)
#NaH
get_Cp_parameter(43,1.5,0.5,1)
#MgH
get_Cp_parameter(44,0,0.5,1)
#AlH
get_Cp_parameter(45,2.5,0.5,1)
#SiH
get_Cp_parameter(46,0,0.5,1)
#PH
get_Cp_parameter(47,0.5,0.5,2)
#HS
get_Cp_parameter(48,0.5,0,2)
#HCl
get_Cp_parameter(49,0.5,1.5,1)
#KH
get_Cp_parameter(50,1.5,0.5,2)


#CaH
get_Cp_parameter(51,0,0.5,1)
#TiH
get_Cp_parameter(52,0,0.5,1)
#CrH
get_Cp_parameter(53,0,0.5,1)
#MnH
get_Cp_parameter(54,2.5,0.5,1)
#FeH
get_Cp_parameter(55,0,0.5,1)
#CoH
get_Cp_parameter(56,3.5,0.5,1)
#NiH
get_Cp_parameter(57,0,0.5,1)
#CuH
get_Cp_parameter(58,1.5,0.5,1)
#ZnH
get_Cp_parameter(59,0,0.5,1)
#GaH
get_Cp_parameter(60,1.5,0.5,1)
#GeH
get_Cp_parameter(61,0,0.5,1)
#AsH
get_Cp_parameter(62,1.5,0.5,1)
#SeH
get_Cp_parameter(63,0,0.5,1)
#HBr
get_Cp_parameter(64,0.5,1.5,1)
#RbH
get_Cp_parameter(65,2.5,0.5,1)
#SrH
get_Cp_parameter(66,0,0.5,1)
#AgH
get_Cp_parameter(67,0.5,0.5,1)
#CdH
get_Cp_parameter(68,0,0.5,1)
#InH
get_Cp_parameter(69,4.5,0.5,1)
#SnH
get_Cp_parameter(70,0,0.5,1)
#SbH
get_Cp_parameter(71,2.5,0.5,1)
#TeH
get_Cp_parameter(72,0,0.5,1)
#HI
get_Cp_parameter(73,0.5,2.5,2)
#CsH
get_Cp_parameter(74,3.5,0.5,1)
#BaH
get_Cp_parameter(75,0,0.5,1)
#YbH
get_Cp_parameter(76,0,0.5,1)
#PtH
get_Cp_parameter(77,0.5,0.5,1)
#AuH
get_Cp_parameter(78,1.5,0.5,1)
#HgH
get_Cp_parameter(79,0,0.5,1)
#TlH
get_Cp_parameter(80,0.5,0.5,1)
#PbH
get_Cp_parameter(81,0,0.5,1)
#BiH
get_Cp_parameter(82,4.5,0.5,1)
#HeH+
get_Cp_parameter(83,0,0.5,1)
#BeH+
get_Cp_parameter(84,1.5,0.5,1)
#CH+
get_Cp_parameter(85,0,0.5,1)
#NH+
get_Cp_parameter(86,1,0.5,1)
#OH+
get_Cp_parameter(87,0,0.5,1)
#HF+
get_Cp_parameter(88,0.5,0.5,1)
#NeH+
get_Cp_parameter(89,0,0.5,1)
#MgH+
get_Cp_parameter(90,0,0.5,1)
#AlH+
get_Cp_parameter(91,2.5,0.5,1)
#SiH+
get_Cp_parameter(92,0,0.5,1)
#PH+
get_Cp_parameter(93,0.5,0.5,1)
#SH+
get_Cp_parameter(94,0,0.5,1)
#HCl+
get_Cp_parameter(95,0.5,1.5,1)
#ZnH+
get_Cp_parameter(96,0,0.5,1)
#HBr+
get_Cp_parameter(97,0.5,1.5,1)
#CdH+
get_Cp_parameter(98,0,0.5,1)
#HgH+
get_Cp_parameter(99,0,0.5,1)
#CH-
get_Cp_parameter(100,0,0.5,1)
#OH-
get_Cp_parameter(101,0,0.5,1)
#SiH-
get_Cp_parameter(102,0,0.5,1)
#HS-
get_Cp_parameter(103,0.5,0,1)



#CN same trend, smaller than janaf table
get_Cp_parameter(104,0,1,2)
#CO fit well
get_Cp_parameter(105,0,0,2)
#CF
get_Cp_parameter(106,0,0.5,2)
#SiC
get_Cp_parameter(107,0,0,1)
#CP
get_Cp_parameter(108,0,0.5,2)
#CS
get_Cp_parameter(109,0,0,2)
#CCl
get_Cp_parameter(110,0,1.5,1)
#CSe
get_Cp_parameter(111,0,0,1)
#CBr
get_Cp_parameter(112,0,1.5,1)
#RhC
get_Cp_parameter(113,0.5,0,1)
#IrC
get_Cp_parameter(114,1.5,0,1)
#PtC
get_Cp_parameter(115,0.5,0,1)
#CN+
get_Cp_parameter(116,0,1,1)

#CO+
get_Cp_parameter(117,0,0,1)
#CN-
get_Cp_parameter(118,0,1,1)
#CS-
get_Cp_parameter(119,0,0,1)

#BN
get_Cp_parameter(120,1.5,1,2)

#NO
get_Cp_parameter(121,1,0,2)

#NF
get_Cp_parameter(122,1,0.5,2)

#AlN 
get_Cp_parameter(123,2.5,1,1)

#SiN
get_Cp_parameter(124,0,1,1)

#PN
get_Cp_parameter(125,0.5,1,2)

#NS
get_Cp_parameter(126,1,0,2)

#NCl
get_Cp_parameter(127,1,1.5,1)

#TiN
get_Cp_parameter(128,0,1,1)

#AsN
get_Cp_parameter(129,1.5,1,1)

#SeN
get_Cp_parameter(130,0,1,1)

#ZrN
get_Cp_parameter(131,0,1,1)

#NO+
get_Cp_parameter(132,1,0,1)

#NS+
get_Cp_parameter(133,1,0,1)

#LiO
get_Cp_parameter(134,1.5,0,1)

#BeO
get_Cp_parameter(135,1.5,0,1)

#BO
get_Cp_parameter(136,1.5,0,2)

#FO
get_Cp_parameter(137,0.5,0,2)

#NaO
get_Cp_parameter(138,1.5,0,1)

#MgO
get_Cp_parameter(139,0,0,1)

#AlO
get_Cp_parameter(140,2.5,0,1)

#SiO
get_Cp_parameter(141,0,0,1)

#PO
get_Cp_parameter(142,0.5,0,2)
#SO
get_Cp_parameter(143,0,0,2)

#ClO
get_Cp_parameter(144,1.5,0,1)
#KO
get_Cp_parameter(145,1.5,0,2)
#CaO
get_Cp_parameter(146,0,0,1)
#ScO
get_Cp_parameter(147,3.5,0,1)
#TiO
get_Cp_parameter(148,0,0,1)
#VO
get_Cp_parameter(149,3.5,0,2)
#CrO
get_Cp_parameter(150,0,0,1)
#MnO
get_Cp_parameter(151,2.5,0,1)
#FeO
get_Cp_parameter(152,0,0,1)
#NiO
get_Cp_parameter(153,0,0,1)
#CuO
get_Cp_parameter(154,1.5,0,1)
#GaO
get_Cp_parameter(155,1.5,0,1)
#GeO
get_Cp_parameter(156,0,0,1)
#AsO
get_Cp_parameter(157,1.5,0,1)
#SeO
get_Cp_parameter(158,0,0,1)
#BrO
get_Cp_parameter(159,1.5,0,1)
#RbO
get_Cp_parameter(160,2.5,0,1)
#SrO
get_Cp_parameter(161,0,0,1)
#YO
get_Cp_parameter(162,0.5,0,2)
#ZrO
get_Cp_parameter(163,0,0,1)
#NbO
get_Cp_parameter(164,4.5,0,1)
#InO
get_Cp_parameter(165,4.5,0,1)
#SnO
get_Cp_parameter(166,0,0,1)
#SbO
get_Cp_parameter(167,2.5,0,1)
#TeO
get_Cp_parameter(168,0,0,1)
#IO
get_Cp_parameter(169,2.5,0,2)
#BaO
get_Cp_parameter(170,0,0,1)
#LaO
get_Cp_parameter(171,3.5,0,1)
#TbO
get_Cp_parameter(172,1.5,0,1)
#LuO
get_Cp_parameter(173,3.5,0,1)
#HfO
get_Cp_parameter(174,0,0,1)
#TaO
get_Cp_parameter(175,3.5,0,1)
#WO
get_Cp_parameter(176,0,0,2)
#PtO
get_Cp_parameter(177,0.5,0,1)
#PbO
get_Cp_parameter(178,0,0,1)
#BiO
get_Cp_parameter(179,4.5,0,1)
#ThO
get_Cp_parameter(180,0,0,1)
#BO+
get_Cp_parameter(181,1.5,0,1)
#SiO+
get_Cp_parameter(182,0,0,1)
#PO+ 
get_Cp_parameter(183,0.5,0,1)
#SO+
get_Cp_parameter(184,0,0,1)
#AsO+
get_Cp_parameter(185,1.5,0,1)
#TaO+
get_Cp_parameter(186,3.5,0,1)
#FeO-
get_Cp_parameter(187,0,0,1)
#LiF
get_Cp_parameter(188,1.5,0.5,1)
#BeF
get_Cp_parameter(189,1.5,0.5,1)
#BF
get_Cp_parameter(190,1.5,0.5,2)
#NaF
get_Cp_parameter(191,1.5,0.5,1)


#MgF
get_Cp_parameter(192,0,0.5,1)
#AlF
get_Cp_parameter(193,2.5,0.5,1)
#SiF
get_Cp_parameter(194,0,0.5,1)
#PF
get_Cp_parameter(195,0.5,0.5,2)
#SF
get_Cp_parameter(196,0,0.5,2)
#KF
get_Cp_parameter(197,1.5,0.5,2)
#CaF
get_Cp_parameter(198,0,0.5,1)
#ScF
get_Cp_parameter(199,3.5,0.5,1)
#MnF
get_Cp_parameter(200,2.5,0.5,1)
#NiF
get_Cp_parameter(201,0,0.5,1)
#CuF
get_Cp_parameter(202,1.5,0.5,1)
#ZnF
get_Cp_parameter(203,0,0.5,1)
#GaF
get_Cp_parameter(204,1.5,0.5,1)
#GeF
get_Cp_parameter(205,0,0.5,1)
#AsF
get_Cp_parameter(206,1.5,0.5,1)
#SeF
get_Cp_parameter(207,0,0.5,1)
#BrF
get_Cp_parameter(208,1.5,0.5,1)
#RbF
get_Cp_parameter(209,2.5,0.5,1)
#SrF
get_Cp_parameter(210,0,0.5,1)
#YF
get_Cp_parameter(211,0.5,0.5,2)
#AgF
get_Cp_parameter(212,0.5,0.5,1)
#CdF
get_Cp_parameter(213,0,0.5,1)
#InF
get_Cp_parameter(214,4.5,0.5,1)
#SnF
get_Cp_parameter(215,0,0.5,1)
#SbF
get_Cp_parameter(216,2.5,0.5,1)
#IF
get_Cp_parameter(217,2.5,0.5,2)
#CsF
get_Cp_parameter(218,3.5,0.5,1)
#BaF
get_Cp_parameter(219,0,0.5,1)
#LaF
get_Cp_parameter(220,3.5,0.5,1)
#HoF
get_Cp_parameter(221,3.5,0.5,1)
#YbF
get_Cp_parameter(222,0,0.5,1)
#LuF
get_Cp_parameter(223,3.5,0.5,1)
#HgF
get_Cp_parameter(224,0,0.5,1)
#TlF
get_Cp_parameter(225,0.5,0.5,1)
#PbF
get_Cp_parameter(226,0,0.5,1)
#LiNa
get_Cp_parameter(227,1.5,1.5,1)
#AsP
get_Cp_parameter(228,1.5,0.5,1)
#SbP
get_Cp_parameter(229,2.5,0.5,1)
#BeS
get_Cp_parameter(230,1.5,0,1)
#BS
get_Cp_parameter(231,1.5,0,2)
#MgS
get_Cp_parameter(232,0,0,1)
#AlS
get_Cp_parameter(233,2.5,0,1)
#SiS
get_Cp_parameter(234,0,0,1)
#PS
get_Cp_parameter(235,0.5,0,2)
#CaS
get_Cp_parameter(236,0,0,1)
#ScS
get_Cp_parameter(237,3.5,0,1)
#TiS
get_Cp_parameter(238,0,0,1)
#CrS
get_Cp_parameter(239,0,0,1)
#CuS
get_Cp_parameter(240,1.5,0,1)
#GeS
get_Cp_parameter(241,0,0,1)
#AsS
get_Cp_parameter(242,1.5,0,1)
#SeS
get_Cp_parameter(243,0,0,1)
#SrS
get_Cp_parameter(244,0,0,1)
#YS
get_Cp_parameter(245,0.5,0,2)
#SnS
get_Cp_parameter(246,0,0,1)
#TeS
get_Cp_parameter(247,0,0,1)
#BaS
get_Cp_parameter(248,0,0,1)
#LaS
get_Cp_parameter(249,3.5,0,1)
#PbS
get_Cp_parameter(250,0,0,1)
#BiS
get_Cp_parameter(251,4.5,0,1)
#LiCl
get_Cp_parameter(252,1.5,1.5,1)
#BeCl
get_Cp_parameter(253,1.5,1.5,1)
#BCl
get_Cp_parameter(254,1.5,1.5,1)
#NaCl
get_Cp_parameter(255,1.5,1.5,1)
#MgCl
get_Cp_parameter(256,0,1.5,1)
#AlCl
get_Cp_parameter(257,2.5,1.5,1)
#SiCl
get_Cp_parameter(258,0,1.5,1)
#PCl
get_Cp_parameter(259,0.5,1.5,1)
#KCl
get_Cp_parameter(260,1.5,1.5,1)
#CaCl
get_Cp_parameter(261,0,1.5,1)
#ScCl
get_Cp_parameter(262,3.5,1.5,1)
#MnCl
get_Cp_parameter(263,2.5,1.5,1)
#FeCl
get_Cp_parameter(264,0,1.5,1)
#CuCl
get_Cp_parameter(265,1.5,1.5,1)
#ZnCl
get_Cp_parameter(266,0,1.5,1)
#GaCl
get_Cp_parameter(267,1.5,1.5,1)
#GeCl
get_Cp_parameter(268,0,1.5,1)
#AsCl
get_Cp_parameter(269,1.5,1.5,1)
#SeCl
get_Cp_parameter(270,0,1.5,1)
#BrCl
get_Cp_parameter(271,1.5,1.5,1)
#RbCl
get_Cp_parameter(272,2.5,1.5,1)
#SrCl
get_Cp_parameter(273,0,1.5,1)
#YCl
get_Cp_parameter(274,0.5,1.5,1)
#AgCl
get_Cp_parameter(275,0.5,1.5,1)
#CdCl
get_Cp_parameter(276,0,1.5,1)
#InCl
get_Cp_parameter(277,4.5,1.5,1)
#SnCl
get_Cp_parameter(278,0,1.5,1)
#SbCl
get_Cp_parameter(279,2.5,1.5,1)
#ICl
get_Cp_parameter(280,2.5,1.5,1)
#CsCl
get_Cp_parameter(281,3.5,1.5,1)
#BaCl
get_Cp_parameter(282,0,1.5,1)
#YbCl
get_Cp_parameter(283,0,1.5,1)
#AuCl
get_Cp_parameter(284,1.5,1.5,1)
#HgCl
get_Cp_parameter(285,0,1.5,1)
#TlCl
get_Cp_parameter(286,0.5,1.5,1)
#PbCl
get_Cp_parameter(287,0,1.5,1)
#AlSe
get_Cp_parameter(288,2.5,0,1)
#SiSe
get_Cp_parameter(289,0,0,1)
#GeSe
get_Cp_parameter(290,0,0,1)
#KBr
get_Cp_parameter(291,1.5,1.5,1)
#SiTe
get_Cp_parameter(292,0,0,1)
#GeTe
get_Cp_parameter(293,0,0,1)
#KI
get_Cp_parameter(294,1.5,2.5,2)
