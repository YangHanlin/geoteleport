# Geoteleport

Redirections based on visitor IP locations.

For example, you can use Geoteleport to redirect visitors to their local CDNs to enhance user experience, especially those not coming from the same provider and not interoperating smoothly. Maybe an inferior choice to DNS-based global CDNs, however, it is rather suitable for me who can only afford Cloudflare Free Plan for integration of Cloudflare's global CDN with Aliyun's CDN in mainland China.

Geoteleport uses [MaxMind GeoLite2](https://dev.maxmind.com/geoip/geoip2/geolite2/) database to tell IP locations, and fits the requirements of a [Vercel serverless function](https://vercel.com/docs/serverless-functions/introduction).

To set up Geoteleport yourself, it is recommended to fork this repo, modify necessary configurations, and deploy this project to Vercel.

[![Deploy to Vercel](https://www.vercel.com/button)](https://vercel.com/import/git?s=https%3A%2F%2Fgithub.com%2FYOUR_USERNAME_HERE%2Fgeoteleport&project-name=geoteleport&repo-name=geoteleport)

## Configuration

### Environment variables

| Name            | Description                           | Default value        |
| --------------- | ------------------------------------- | -------------------- |
| `GEOIP_DB_PATH` | Path to the GeoLite2 Country database | `/db/Country.mmdb`   |
| `CONFIG_PATH`   | Path to the configuration file        | `/config/rules.json` |

### Configuration file

Geoteleport uses rules defined in the configuration file to tell which redirection to send. Below is an [example](config/rules.json):

```jsonc
{
  // Rules are defined under the key 'rules'
  "rules": [
    // Rules (except the last rule) define IP regions and their corresponding
    // redirections
    {
      // name: required, string, name of the rule
      "name": "domestic",
      // regions: required, array of strings, IP regions this rule covers
      "regions": [
        "CN"
      ],
      // redirect: required, string, template to construct redirected urls
      "redirect": "{scheme}://sites.tree-diagram.space/{path}"
    },
    // The last rule is a fallback rule that matches any request that does not
    // match any of the rules above
    {
      "name": "global",
      "redirect": "{scheme}://sites.tree-diagram.site/{path}"
    }
  ]
}
```

## License

The use and distribution of [MaxMind GeoLite2 database](db/Country.mmdb) is licensed under its [EULA](https://www.maxmind.com/en/geolite2/eula).

All other contents in this repository, unless otherwise noted, are licensed under [MIT](LICENSE).