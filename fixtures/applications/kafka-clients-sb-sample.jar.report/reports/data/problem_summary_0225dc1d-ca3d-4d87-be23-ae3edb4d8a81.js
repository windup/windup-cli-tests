MIGRATION_ISSUES_DETAILS["0225dc1d-ca3d-4d87-be23-ae3edb4d8a81"] = [
{description: "<p>Check if there is a Quarkus Extensions with Spring API compatibility for the Spring <code>spring-kafka-test<\/code> component.<br/> If yes, then replace the <code>org.springframework.kafka:spring-kafka-test<\/code> dependency with the Quarkus extension.<br/> If no, consider rewrite the code that relies on this dependency leveraging the Quarkus Guides linked below.<\/p>", ruleID: "springboot-generic-catchall-groovy-00000", issueName: "Spring component spring-kafka-test requires investigation",
problemSummaryID: "0225dc1d-ca3d-4d87-be23-ae3edb4d8a81", files: [
{l:"<a class='' href='pom_xml.html?project=4423800'>META-INF/maven/com.rmarting.kafka/kafka-clients-sb-sample/pom.xml<\/a>", oc:"1"},
], resourceLinks: [
{h:"https://quarkus.io/guides/", t:"Quarkus - Guides"},
]},
];
onProblemSummaryLoaded("0225dc1d-ca3d-4d87-be23-ae3edb4d8a81");