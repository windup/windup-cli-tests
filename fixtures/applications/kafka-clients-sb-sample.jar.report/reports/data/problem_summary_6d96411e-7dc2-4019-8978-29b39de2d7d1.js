MIGRATION_ISSUES_DETAILS["6d96411e-7dc2-4019-8978-29b39de2d7d1"] = [
{description: "<p>Check if there is a Quarkus Extensions with Spring API compatibility for the Spring <code>spring-integration-zookeeper<\/code> component.<br/> If yes, then replace the <code>org.springframework.integration:spring-integration-zookeeper<\/code> dependency with the Quarkus extension.<br/> If no, consider rewrite the code that relies on this dependency leveraging the Quarkus Guides linked below.<\/p>", ruleID: "springboot-generic-catchall-groovy-00000", issueName: "Spring component spring-integration-zookeeper requires investigation",
problemSummaryID: "6d96411e-7dc2-4019-8978-29b39de2d7d1", files: [
{l:"<a class='' href='pom_xml.html?project=4423800'>META-INF/maven/com.rmarting.kafka/kafka-clients-sb-sample/pom.xml<\/a>", oc:"1"},
], resourceLinks: [
{h:"https://quarkus.io/guides/", t:"Quarkus - Guides"},
]},
];
onProblemSummaryLoaded("6d96411e-7dc2-4019-8978-29b39de2d7d1");