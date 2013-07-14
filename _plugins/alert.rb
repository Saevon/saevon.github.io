class Jekyll::Alert < Liquid::Block
    alias_method :render_block, :render

    DIVIDER = '\n\n<!-- GENERATED TEMPORARY ALERT DIVIDER -->\n\n'
    LEVEL_TO_ICON = {
        'info' => 'info-sign',
        'warning' => 'warning-sign',
        'error' => 'remove',
        'success' => 'ok',
    }

    def initialize(tag, markup, tokens)
        if markup =~ /(?<level>info|error|warning|success)?\s*(icon=(?<icon>(nil|".*")))?/i
            level = Regexp.last_match(:level)
            icon = Regexp.last_match(:icon)

            if level == ''
                @level = 'info'
            else
                @level = level
            end

            if icon == 'nil'
                @icon = nil
            elsif not icon
                @icon = LEVEL_TO_ICON[@level]
            else
                # Strip out the quotes
                @icon = icon[1..-2]
            end
        end
        super
    end

    def render(context)
        # Figure out which converter to use on the content
        site = context.registers[:site]
        page = context.registers[:page]

        ext = File.extname(page["path"])
        converter =  site.converters.find { |c| c.matches(ext) }

        # Convert the contents with the original page as context
        # In case you have footnotes or other such links
        text = converter.convert(page["content"] + DIVIDER + super)
        text = text.split(DIVIDER)[1]


        # Render the actual alert tag now
        html = '<div class="alert alert-block alert-' + @level + '">'
        if @icon != nil
            html << ' <i class="icon-' + @icon + '"> </i> '
        end

        html << text
        html << '</div>'

        return html
    end
end


Liquid::Template.register_tag('alert', Jekyll::Alert)
