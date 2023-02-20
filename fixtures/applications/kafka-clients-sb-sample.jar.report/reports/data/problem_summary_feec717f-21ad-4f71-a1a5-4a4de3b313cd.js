MIGRATION_ISSUES_DETAILS["feec717f-21ad-4f71-a1a5-4a4de3b313cd"] = [
{description: "<p>Check if there is a Quarkus Extensions with Spring API compatibility for the Spring <code>spring-boot<\/code> component.<br/> If yes, then replace the <code>org.springframework.boot:spring-boot<\/code> dependency with the Quarkus extension.<br/> If no, consider rewrite the code that relies on this dependency leveraging the Quarkus Guides linked below.<\/p>", ruleID: "springboot-generic-catchall-groovy-00000", issueName: "Spring component spring-boot requires investigation",
problemSummaryID: "feec717f-21ad-4f71-a1a5-4a4de3b313cd", files: [
{l:"<a class='' href='pom_xml.41.html?project=4423800'>META-INF/maven/org.webjars/webjars-locator-core/pom.xml<\/a>", oc:"1"},
], resourceLinks: [
{h:"https://quarkus.io/guides/", t:"Quarkus - Guides"},
]},
];
onProblemSummaryLoaded("feec717f-21ad-4f71-a1a5-4a4de3b313cd");