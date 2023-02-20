MIGRATION_ISSUES_DETAILS["05619bd4-2f92-4f88-8a87-a49371fe37c2"] = [
{description: "<p>Check if there is a Quarkus Extensions with Spring API compatibility for the Spring <code>spring-boot-loader-tools<\/code> component.<br/> If yes, then replace the <code>org.springframework.boot:spring-boot-loader-tools<\/code> dependency with the Quarkus extension.<br/> If no, consider rewrite the code that relies on this dependency leveraging the Quarkus Guides linked below.<\/p>", ruleID: "springboot-generic-catchall-groovy-00000", issueName: "Spring component spring-boot-loader-tools requires investigation",
problemSummaryID: "05619bd4-2f92-4f88-8a87-a49371fe37c2", files: [
{l:"<a class='' href='pom_xml.41.html?project=4423800'>META-INF/maven/org.webjars/webjars-locator-core/pom.xml<\/a>", oc:"1"},
], resourceLinks: [
{h:"https://quarkus.io/guides/", t:"Quarkus - Guides"},
]},
];
onProblemSummaryLoaded("05619bd4-2f92-4f88-8a87-a49371fe37c2");