MIGRATION_ISSUES_DETAILS["5ea56921-b292-40e7-adc8-2e1d09d90878"] = [
{description: "<p>Check if there is a Quarkus Extensions with Spring API compatibility for the Spring <code>spring-boot-maven-plugin<\/code> component.<br/> If yes, then replace the <code>org.springframework.boot:spring-boot-maven-plugin<\/code> dependency with the Quarkus extension.<br/> If no, consider rewrite the code that relies on this dependency leveraging the Quarkus Guides linked below.<\/p>", ruleID: "springboot-generic-catchall-groovy-00000", issueName: "Spring component spring-boot-maven-plugin requires investigation",
problemSummaryID: "5ea56921-b292-40e7-adc8-2e1d09d90878", files: [
{l:"<a class='' href='pom_xml.html?project=4423800'>META-INF/maven/com.rmarting.kafka/kafka-clients-sb-sample/pom.xml<\/a>", oc:"1"},
], resourceLinks: [
{h:"https://quarkus.io/guides/", t:"Quarkus - Guides"},
]},
];
onProblemSummaryLoaded("5ea56921-b292-40e7-adc8-2e1d09d90878");