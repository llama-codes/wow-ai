export const RATE_LIMIT_QUERY = /* GraphQL */ `
  query WarcraftLogsRateLimit {
    rateLimitData {
      limitPerHour
      pointsSpentThisHour
      pointsResetIn
    }
  }
`;

export const REPORT_SUMMARY_QUERY = /* GraphQL */ `
  query WarcraftLogsReportSummary($code: String!, $allowUnlisted: Boolean) {
    reportData {
      report(code: $code, allowUnlisted: $allowUnlisted) {
        code
        endTime
        exportedSegments
        revision
        segments
        startTime
        title
        visibility
      }
    }
  }
`;

export const REPORT_FIGHTS_QUERY = /* GraphQL */ `
  query WarcraftLogsReportFights(
    $code: String!
    $allowUnlisted: Boolean
    $difficulty: Int
    $encounterID: Int
    $fightIDs: [Int]
    $killType: KillType
    $translate: Boolean
  ) {
    reportData {
      report(code: $code, allowUnlisted: $allowUnlisted) {
        fights(
          difficulty: $difficulty
          encounterID: $encounterID
          fightIDs: $fightIDs
          killType: $killType
          translate: $translate
        ) {
          id
          name
          startTime
          endTime
          encounterID
          kill
          difficulty
        }
      }
    }
  }
`;

export const REPORT_MASTER_DATA_QUERY = /* GraphQL */ `
  query WarcraftLogsReportMasterData(
    $code: String!
    $allowUnlisted: Boolean
    $translate: Boolean
    $actorType: String
    $actorSubType: String
  ) {
    reportData {
      report(code: $code, allowUnlisted: $allowUnlisted) {
        masterData(translate: $translate) {
          logVersion
          gameVersion
          lang
          abilities {
            gameID
            icon
            name
            type
          }
          actors(type: $actorType, subType: $actorSubType) {
            gameID
            icon
            id
            name
            petOwner
            server
            subType
            type
          }
        }
      }
    }
  }
`;

export const REPORT_EVENTS_QUERY = /* GraphQL */ `
  query WarcraftLogsReportEvents(
    $code: String!
    $allowUnlisted: Boolean
    $abilityID: Float
    $dataType: EventDataType
    $death: Int
    $difficulty: Int
    $encounterID: Int
    $endTime: Float
    $fightIDs: [Int]
    $filterExpression: String
    $hostilityType: HostilityType
    $includeResources: Boolean
    $killType: KillType
    $limit: Int
    $sourceAurasAbsent: String
    $sourceAurasPresent: String
    $sourceClass: String
    $sourceID: Int
    $sourceInstanceID: Int
    $startTime: Float
    $targetAurasAbsent: String
    $targetAurasPresent: String
    $targetClass: String
    $targetID: Int
    $targetInstanceID: Int
    $translate: Boolean
    $useAbilityIDs: Boolean
    $useActorIDs: Boolean
    $viewOptions: Int
    $wipeCutoff: Int
  ) {
    reportData {
      report(code: $code, allowUnlisted: $allowUnlisted) {
        events(
          abilityID: $abilityID
          dataType: $dataType
          death: $death
          difficulty: $difficulty
          encounterID: $encounterID
          endTime: $endTime
          fightIDs: $fightIDs
          filterExpression: $filterExpression
          hostilityType: $hostilityType
          includeResources: $includeResources
          killType: $killType
          limit: $limit
          sourceAurasAbsent: $sourceAurasAbsent
          sourceAurasPresent: $sourceAurasPresent
          sourceClass: $sourceClass
          sourceID: $sourceID
          sourceInstanceID: $sourceInstanceID
          startTime: $startTime
          targetAurasAbsent: $targetAurasAbsent
          targetAurasPresent: $targetAurasPresent
          targetClass: $targetClass
          targetID: $targetID
          targetInstanceID: $targetInstanceID
          translate: $translate
          useAbilityIDs: $useAbilityIDs
          useActorIDs: $useActorIDs
          viewOptions: $viewOptions
          wipeCutoff: $wipeCutoff
        ) {
          data
          nextPageTimestamp
        }
      }
    }
  }
`;

export const REPORT_TABLE_QUERY = /* GraphQL */ `
  query WarcraftLogsReportTable(
    $code: String!
    $allowUnlisted: Boolean
    $abilityID: Float
    $dataType: TableDataType
    $death: Int
    $difficulty: Int
    $encounterID: Int
    $endTime: Float
    $fightIDs: [Int]
    $filterExpression: String
    $hostilityType: HostilityType
    $killType: KillType
    $sourceAurasAbsent: String
    $sourceAurasPresent: String
    $sourceClass: String
    $sourceID: Int
    $sourceInstanceID: Int
    $startTime: Float
    $targetAurasAbsent: String
    $targetAurasPresent: String
    $targetClass: String
    $targetID: Int
    $targetInstanceID: Int
    $translate: Boolean
    $viewOptions: Int
    $viewBy: ViewType
    $wipeCutoff: Int
  ) {
    reportData {
      report(code: $code, allowUnlisted: $allowUnlisted) {
        table(
          abilityID: $abilityID
          dataType: $dataType
          death: $death
          difficulty: $difficulty
          encounterID: $encounterID
          endTime: $endTime
          fightIDs: $fightIDs
          filterExpression: $filterExpression
          hostilityType: $hostilityType
          killType: $killType
          sourceAurasAbsent: $sourceAurasAbsent
          sourceAurasPresent: $sourceAurasPresent
          sourceClass: $sourceClass
          sourceID: $sourceID
          sourceInstanceID: $sourceInstanceID
          startTime: $startTime
          targetAurasAbsent: $targetAurasAbsent
          targetAurasPresent: $targetAurasPresent
          targetClass: $targetClass
          targetID: $targetID
          targetInstanceID: $targetInstanceID
          translate: $translate
          viewOptions: $viewOptions
          viewBy: $viewBy
          wipeCutoff: $wipeCutoff
        )
      }
    }
  }
`;

export const REPORT_RANKINGS_QUERY = /* GraphQL */ `
  query WarcraftLogsReportRankings(
    $code: String!
    $allowUnlisted: Boolean
    $compare: RankingCompareType
    $difficulty: Int
    $encounterID: Int
    $fightIDs: [Int]
    $playerMetric: ReportRankingMetricType
    $timeframe: RankingTimeframeType
  ) {
    reportData {
      report(code: $code, allowUnlisted: $allowUnlisted) {
        rankings(
          compare: $compare
          difficulty: $difficulty
          encounterID: $encounterID
          fightIDs: $fightIDs
          playerMetric: $playerMetric
          timeframe: $timeframe
        )
      }
    }
  }
`;
