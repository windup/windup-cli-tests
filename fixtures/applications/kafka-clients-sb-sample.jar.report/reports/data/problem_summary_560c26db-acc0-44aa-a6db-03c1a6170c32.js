MIGRATION_ISSUES_DETAILS["560c26db-acc0-44aa-a6db-03c1a6170c32"] = [
{description: "<p>Check if there is a Quarkus Extensions with Spring API compatibility for the Spring <code>springdoc-openapi-ui<\/code> component.<br/> If yes, then replace the <code>org.springdoc:springdoc-openapi-ui<\/code> dependency with the Quarkus extension.<br/> If no, consider rewrite the code that relies on this dependency leveraging the Quarkus Guides linked below.<\/p>", ruleID: "springboot-generic-catchall-groovy-00000", issueName: "Spring component springdoc-openapi-ui requires investigation",
problemSummaryID: "560c26db-acc0-44aa-a6db-03c1a6170c32", files: [
{l:"<a class='' href='pom_xml.html?project=4423800'>META-INF/maven/com.rmarting.kafka/kafka-clients-sb-sample/pom.xml<\/a>", oc:"1"},
], resourceLinks: [
{h:"https://quarkus.io/guides/", t:"Quarkus - Guides"},
]},
];
onProblemSummaryLoaded("560c26db-acc0-44aa-a6db-03c1a6170c32");