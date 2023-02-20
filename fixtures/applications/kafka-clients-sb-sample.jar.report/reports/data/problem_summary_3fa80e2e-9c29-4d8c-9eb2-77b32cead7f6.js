MIGRATION_ISSUES_DETAILS["3fa80e2e-9c29-4d8c-9eb2-77b32cead7f6"] = [
{description: "<p>Check if there is a Quarkus Extensions with Spring API compatibility for the Spring <code>spring-kafka<\/code> component.<br/> If yes, then replace the <code>org.springframework.kafka:spring-kafka<\/code> dependency with the Quarkus extension.<br/> If no, consider rewrite the code that relies on this dependency leveraging the Quarkus Guides linked below.<\/p>", ruleID: "springboot-generic-catchall-groovy-00000", issueName: "Spring component spring-kafka requires investigation",
problemSummaryID: "3fa80e2e-9c29-4d8c-9eb2-77b32cead7f6", files: [
{l:"<a class='' href='pom_xml.html?project=4423800'>META-INF/maven/com.rmarting.kafka/kafka-clients-sb-sample/pom.xml<\/a>", oc:"1"},
], resourceLinks: [
{h:"https://quarkus.io/guides/", t:"Quarkus - Guides"},
]},
];
onProblemSummaryLoaded("3fa80e2e-9c29-4d8c-9eb2-77b32cead7f6");