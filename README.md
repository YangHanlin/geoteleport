# Geoteleport

Redirections based on visitor IP locations.

For example, you can use Geoteleport to redirect visitors to their local CDNs to enhance user experience, especially those not coming from the same provider and not interoperating smoothly. Maybe an inferior choice to DNS-based global CDNs, however, it is rather suitable for me who can only afford Cloudflare Free Plan for integration of Cloudflare's global CDN with Aliyun's CDN in mainland China.

Geoteleport uses [MaxMind GeoLite2](https://dev.maxmind.com/geoip/geoip2/geolite2/) database to tell IP locations, and fits the requirements of a [Vercel serverless function](https://vercel.com/docs/serverless-functions/introduction) (you can directly [import](https://vercel.com/import) this repo after modifying configuration).

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
      "redirect": "{scheme}://domestic-pages.tree-diagram.site/{path}"
    },
    // The last rule is a fallback rule that matches any request that does not
    // match any of the rules above
    {
      "name": "global",
      "redirect": "{scheme}://global-pages.tree-diagram.site/{path}"
    }
  ]
}
```

## License

The use and distribution of [MaxMind GeoLite2 database](db/Country.mmdb) is licensed under its [EULA](https://www.maxmind.com/en/geolite2/eula).

All other contents in this repository, unless otherwise noted, are licensed under [MIT](LICENSE).