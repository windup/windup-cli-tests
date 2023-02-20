MIGRATION_ISSUES_DETAILS["6a062ed8-10bf-445f-aa2b-36b2ae3606b3"] = [
{description: "<p>Check if there is a Quarkus Extensions with Spring API compatibility for the Spring <code>spring-boot-starter-parent<\/code> component.<br/> If yes, then replace the <code>org.springframework.boot:spring-boot-starter-parent<\/code> dependency with the Quarkus extension.<br/> If no, consider rewrite the code that relies on this dependency leveraging the Quarkus Guides linked below.<\/p>", ruleID: "springboot-generic-catchall-groovy-00000", issueName: "Spring component spring-boot-starter-parent requires investigation",
problemSummaryID: "6a062ed8-10bf-445f-aa2b-36b2ae3606b3", files: [
{l:"<a class='' href='pom_xml.html?project=4423800'>META-INF/maven/com.rmarting.kafka/kafka-clients-sb-sample/pom.xml<\/a>", oc:"1"},
], resourceLinks: [
{h:"https://quarkus.io/guides/", t:"Quarkus - Guides"},
]},
];
onProblemSummaryLoaded("6a062ed8-10bf-445f-aa2b-36b2ae3606b3");