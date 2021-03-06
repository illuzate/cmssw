import FWCore.ParameterSet.Config as cms

l1tSummaryStage2HltDigis = cms.EDAnalyzer(
    "L1TSummary",
    tag        = cms.string("Stage 2 Digis Unpacked by HLT L1 unpack sequence"),
    egCheck    = cms.bool(True),
    tauCheck   = cms.bool(True),
    jetCheck   = cms.bool(True),
    sumCheck   = cms.bool(True),
    muonCheck  = cms.bool(True),
    bxZeroOnly = cms.bool(True),
    egToken    = cms.InputTag("hltCaloStage2Digis"),
    tauTokens  = cms.VInputTag("hltCaloStage2Digis"),
    jetToken   = cms.InputTag("hltCaloStage2Digis"),
    sumToken   = cms.InputTag("hltCaloStage2Digis"),
    muonToken  = cms.InputTag("hltGmtStage2Digis",""),
)
