// @ts-nocheck

/**@constructor*/
// @ts-ignore
BaseStemmer = function() {
    /** @protected */
    // @ts-ignore
    this.current = '';
    this.cursor = 0;
    this.limit = 0;
    this.limit_backward = 0;
    this.bra = 0;
    this.ket = 0;

    /**
     * @param {string} value
     */
    this.setCurrent = function(value) {
        this.current = value;
        this.cursor = 0;
        this.limit = this.current.length;
        this.limit_backward = 0;
        this.bra = this.cursor;
        this.ket = this.limit;
    };

    /**
     * @return {string}
     */
    this.getCurrent = function() {
        // @ts-ignore
        return this.current;
    };

    /**
     * @param {BaseStemmer} other
     */
    this.copy_from = function(other) {
        /** @protected */
        // @ts-ignore
        this.current          = other.current;
        this.cursor           = other.cursor;
        this.limit            = other.limit;
        this.limit_backward   = other.limit_backward;
        this.bra              = other.bra;
        this.ket              = other.ket;
    };

    /**
     * @param {number[]} s
     * @param {number} min
     * @param {number} max
     * @return {boolean}
     */
    this.in_grouping = function(s, min, max) {
        /** @protected */
        if (this.cursor >= this.limit) return false;
        // @ts-ignore
        let ch = this.current.codePointAt(this.cursor);
        if (ch > max || ch < min) return false;
        ch -= min;
        if ((s[ch >>> 3] & (0x1 << (ch & 0x7))) == 0) return false;
        this.cursor++;
        return true;
    };

    /**
     * @param {number[]} s
     * @param {number} min
     * @param {number} max
     * @return {boolean}
     */
    this.go_in_grouping = function(s, min, max) {
        /** @protected */
        while (this.cursor < this.limit) {
            // @ts-ignore
            let ch = this.current.codePointAt(this.cursor);
            if (ch > max || ch < min)
                return true;
            ch -= min;
            if ((s[ch >>> 3] & (0x1 << (ch & 0x7))) == 0)
                return true;
            this.cursor++;
        }
        return false;
    };

    /**
     * @param {number[]} s
     * @param {number} min
     * @param {number} max
     * @return {boolean}
     */
    this.in_grouping_b = function(s, min, max) {
        /** @protected */
        if (this.cursor <= this.limit_backward) return false;
        // @ts-ignore
        let ch = this.current.codePointAt(this.cursor - 1);
        if (ch > max || ch < min) return false;
        ch -= min;
        if ((s[ch >>> 3] & (0x1 << (ch & 0x7))) == 0) return false;
        this.cursor--;
        return true;
    };

    /**
     * @param {number[]} s
     * @param {number} min
     * @param {number} max
     * @return {boolean}
     */
    this.go_in_grouping_b = function(s, min, max) {
        /** @protected */
        while (this.cursor > this.limit_backward) {
            // @ts-ignore
            let ch = this.current.codePointAt(this.cursor - 1);
            if (ch > max || ch < min) return true;
            ch -= min;
            if ((s[ch >>> 3] & (0x1 << (ch & 0x7))) == 0) return true;
            this.cursor--;
        }
        return false;
    };

    /**
     * @param {number[]} s
     * @param {number} min
     * @param {number} max
     * @return {boolean}
     */
    this.out_grouping = function(s, min, max) {
        /** @protected */
        if (this.cursor >= this.limit) return false;
        // @ts-ignore
        let ch = this.current.codePointAt(this.cursor);
        if (ch > max || ch < min) {
            this.cursor++;
            return true;
        }
        ch -= min;
        if ((s[ch >>> 3] & (0X1 << (ch & 0x7))) == 0) {
            this.cursor++;
            return true;
        }
        return false;
    };

    /**
     * @param {number[]} s
     * @param {number} min
     * @param {number} max
     * @return {boolean}
     */
    this.go_out_grouping = function(s, min, max) {
        /** @protected */
        while (this.cursor < this.limit) {
            // @ts-ignore
            let ch = this.current.codePointAt(this.cursor);
            if (ch <= max && ch >= min) {
                ch -= min;
                if ((s[ch >>> 3] & (0X1 << (ch & 0x7))) != 0) {
                    return true;
                }
            }
            this.cursor++;
        }
        return false;
    };

    /**
     * @param {number[]} s
     * @param {number} min
     * @param {number} max
     * @return {boolean}
     */
    this.out_grouping_b = function(s, min, max) {
        /** @protected */
        if (this.cursor <= this.limit_backward) return false;
        // @ts-ignore
        let ch = this.current.codePointAt(this.cursor - 1);
        if (ch > max || ch < min) {
            this.cursor--;
            return true;
        }
        ch -= min;
        if ((s[ch >>> 3] & (0x1 << (ch & 0x7))) == 0) {
            this.cursor--;
            return true;
        }
        return false;
    };

    /**
     * @param {number[]} s
     * @param {number} min
     * @param {number} max
     * @return {boolean}
     */
    this.go_out_grouping_b = function(s, min, max) {
        /** @protected */
        while (this.cursor > this.limit_backward) {
            // @ts-ignore
            let ch = this.current.codePointAt(this.cursor - 1);
            if (ch <= max && ch >= min) {
                ch -= min;
                if ((s[ch >>> 3] & (0x1 << (ch & 0x7))) != 0) {
                    return true;
                }
            }
            this.cursor--;
        }
        return false;
    };

    /**
     * @param {string} s
     * @return {boolean}
     */
    this.eq_s = function(s)
    {
        /** @protected */
        if (this.limit - this.cursor < s.length) return false;
        // @ts-ignore
        if (this.current.slice(this.cursor, this.cursor + s.length) != s)
        {
            return false;
        }
        this.cursor += s.length;
        return true;
    };

    /**
     * @param {string} s
     * @return {boolean}
     */
    this.eq_s_b = function(s)
    {
        /** @protected */
        if (this.cursor - this.limit_backward < s.length) return false;
        // @ts-ignore
        if (this.current.slice(this.cursor - s.length, this.cursor) != s)
        {
            return false;
        }
        this.cursor -= s.length;
        return true;
    };

    /**
     * @param {Among[]} v
     * @return {number}
     */
    this.find_among = function(v)
    {
        /** @protected */
        let i = 0;
        let j = v.length;

        let c = this.cursor;
        // @ts-ignore
        let l = this.limit;

        let common_i = 0;
        let common_j = 0;

        let first_key_inspected = false;

        while (true)
        {
            let k = i + ((j - i) >>> 1);
            let diff = 0;
            let common = Math.min(common_i, common_j); // smaller
            // w[0]: string, w[1]: substring_i, w[2]: result, w[3]: function (optional)
            let w = v[k];
            let i2;
            for (i2 = common; i2 < w[0].length; i2++)
            {
                // @ts-ignore
                if (c + common == l)
                {
                    diff = -1;
                    break;
                }
                // @ts-ignore
                diff = this.current.codePointAt(c + common) - w[0].codePointAt(i2);
                if (diff != 0) break;
                common++;
            }
            if (diff < 0)
            {
                j = k;
                common_j = common;
            }
            else
            {
                i = k;
                common_i = common;
            }
            if (j - i <= 1)
            {
                if (i > 0) break; // v->s has been inspected
                if (j == i) break; // only one item in v

                // - but now we need to go round once more to get
                // v->s inspected. This looks messy, but is actually
                // the optimal approach.

                if (first_key_inspected) break;
                first_key_inspected = true;
            }
        }
        do {
            let w = v[i];
            if (common_i >= w[0].length)
            {
                this.cursor = c + w[0].length;
                if (w.length < 4) return w[2];
                let res = w[3](this);
                this.cursor = c + w[0].length;
                if (res) return w[2];
            }
            i = w[1];
        } while (i >= 0);
        return 0;
    };

    // find_among_b is for backwards processing. Same comments apply
    /**
     * @param {Among[]} v
     * @return {number}
     */
    this.find_among_b = function(v)
    {
        /** @protected */
        let i = 0;
        let j = v.length

        let c = this.cursor;
        // @ts-ignore
        let lb = this.limit_backward;

        let common_i = 0;
        let common_j = 0;

        let first_key_inspected = false;

        while (true)
        {
            let k = i + ((j - i) >> 1);
            let diff = 0;
            let common = Math.min(common_i, common_j);
            let w = v[k];
            let i2;
            for (i2 = w[0].length - 1 - common; i2 >= 0; i2--)
            {
                // @ts-ignore
                if (c - common == lb)
                {
                    diff = -1;
                    break;
                }
                // @ts-ignore
                diff = this.current.codePointAt(c - 1 - common) - w[0].codePointAt(i2);
                if (diff != 0) break;
                common++;
            }
            if (diff < 0)
            {
                j = k;
                common_j = common;
            }
            else
            {
                i = k;
                common_i = common;
            }
            if (j - i <= 1)
            {
                if (i > 0) break;
                if (j == i) break;
                if (first_key_inspected) break;
                first_key_inspected = true;
            }
        }
        do {
            let w = v[i];
            if (common_i >= w[0].length)
            {
                // @ts-ignore
                this.cursor = c - w[0].length;
                if (w.length < 4) return w[2];
                let res = w[3](this);
                // @ts-ignore
                this.cursor = c - w[0].length;
                if (res) return w[2];
            }
            i = w[1];
        } while (i >= 0);
        return 0;
    };

    /* to replace chars between c_bra and c_ket in this.current by the
     * chars in s.
     */
    /**
     * @param {number} c_bra
     * @param {number} c_ket
     * @param {string} s
     * @return {number}
     */
    this.replace_s = function(c_bra, c_ket, s)
    {
        /** @protected */
        let adjustment = s.length - (c_ket - c_bra);
        // @ts-ignore
        this.current = this.current.slice(0, c_bra) + s + this.current.slice(c_ket);
        // @ts-ignore
        this.limit += adjustment;
        // @ts-ignore
        if (this.cursor >= c_ket) this.cursor += adjustment;
        // @ts-ignore
        else if (this.cursor > c_bra) this.cursor = c_bra;
        return adjustment;
    };

    /**
     * @return {boolean}
     */
    this.slice_check = function()
    {
        /** @protected */
        if (this.bra < 0 ||
            this.bra > this.ket ||
            this.ket > this.limit ||
            // @ts-ignore
            this.limit > this.current.length)
        {
            return false;
        }
        return true;
    };

    /**
     * @param {number} c_bra
     * @return {boolean}
     */
    // @ts-ignore
    this.slice_from = function(s)
    {
        /** @protected */
        let result = false;
        if (this.slice_check())
        {
            this.replace_s(this.bra, this.ket, s);
            result = true;
        }
        return result;
    };

    /**
     * @return {boolean}
     */
    this.slice_del = function()
    {
        /** @protected */
        return this.slice_from("");
    };

    /**
     * @param {number} c_bra
     * @param {number} c_ket
     * @param {string} s
     */
    this.insert = function(c_bra, c_ket, s)
    {
        /** @protected */
        let adjustment = this.replace_s(c_bra, c_ket, s);
        if (c_bra <= this.bra) this.bra += adjustment;
        if (c_bra <= this.ket) this.ket += adjustment;
    };

    /**
     * @return {string}
     */
    this.slice_to = function()
    {
        /** @protected */
        let result = '';
        if (this.slice_check())
        {
            // @ts-ignore
            result = this.current.slice(this.bra, this.ket);
        }
        return result;
    };

    /**
     * @return {string}
     */
    this.assign_to = function()
    {
        /** @protected */
        // @ts-ignore
        return this.current.slice(0, this.limit);
    };
};
